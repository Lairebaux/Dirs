import os
import pprint
import filecmp
import glob

ext1 = "txt"
ext2 = "py"
msg1 = "Bonjour"
msg2 = "Bonjour2"

def create_file(file_name, text, ext=ext1):
    """create and write to files"""
    condition = "a" if os.path.exists(file_name) else "w"
    with open(f"{file_name}.{ext}", condition) as out_file:
        out_file.write(text)

def make_dir_sub_dir(dir_names, sub_names, file_name):
    num = 0
    while num < 4:
        if not os.path.exists(f"{dir_names}{num}/{sub_names}{num}"):
            os.makedirs(f"{dir_names}{num}/{sub_names}{num}")
        create_file(f"{dir_names}{num}/{sub_names}{num}/{file_name}{num}", msg1)
        if num >= 2 :
            create_file(f"{dir_names}{num}/{sub_names}{num}/{file_name}{num}", msg2, ext=ext2)
        num += 1

def rename_files(current_dir, old_path, new_path):
    os.chdir(current_dir)
    os.rename(old_path, new_path)

def get_current_path():
    print(os.getcwd())

def display_objects_in_dir():
    """list entries in path"""
    print(os.listdir("."))

def display_specific_files(regex):
    """display files with matching regex"""
    for file in glob.glob(regex):
        print(file)

def remove_all_dirs(path):
    """remove parent directories and its children"""
    for dir in glob.glob(path):
        os.removedirs(dir)

def remove_files(regex):
    """remove files with matching regex"""
    for file in glob.glob(regex):
        os.remove(file)

def list_files_in_spec_dirs(dir1, dir2):
    """compare files between directories; left=dir1 right=dir2"""
    files = filecmp.dircmp(dir1, dir2)
    print(f"{dir1}")
    print(files.left_list)
    print(f"\n{dir2}")
    print(files.right_list)

def compare_files_in_dir(dir1, dir2,):
    d1 = set(os.listdir(dir1))
    d2 = set(os.listdir(dir2))
    sets = list(d1 & d2)
    identical_files = [files for files in sets if os.path.isfile(os.path.join(dir1, files))]
    filecmp.dircmp(dir1, dir2).report_full_closure()

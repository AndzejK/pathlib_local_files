from pathlib import Path

root_dit=Path("files")
file_paths=root_dit.iterdir()

"""
path_to_file_3=Path("files/file_3.txt")
if not path_to_file_3.exists(): # if the file does not exist then create a file
    with open(path_to_file_3,"w") as file:
        (file.write("#3 Random contect "))
"""
for path in file_paths:
    new_filename='new_'+path.stem+path.suffix # Stem - just the name of the file; Suffix -> extention
    new_filename=path.with_name(new_filename) #get the path of the files using with_name !!!
    path.rename(new_filename)
# print(root_dit.cwd()) ### CWD - currant working dictionary same as resolve() will display full path



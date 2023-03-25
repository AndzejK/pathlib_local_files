from pathlib import Path

root_dir=Path("files")

#1 way of looping dictionaries
"""
file_paths=root_dir.iterdir()
for file_path in file_paths:
    if file_path.is_dir(): # checking if this file is dictionary
        for file in file_path.iterdir():
            print(file)
    else:
        print(file_path)
"""

#2 way of looping dictionaries
file_paths=root_dir.glob("*/*") # glob allows me to easily find files or directories matching a specified pattern.
                                # The first part * matches any name for the top-level directory, 
                                # and the second part * matches any name for the second-level directory or file.
for path in file_paths:
    if path.is_file(): # checking if this file is NOT dictionary
        parent_dic=path.parts[-2]
        new_file_name=parent_dic+"-"+path.name # new name for a file
        new_filepath=path.with_name(new_file_name) # takes a new name and keeps this file in the same place "with_name" method
        path.rename(new_filepath)
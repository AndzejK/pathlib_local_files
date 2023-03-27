from pathlib import Path

root_dir="txt_files_from_A_to_Z"

for i in range(ord('a'), ord('z')+1):
    filename=chr(i)+".txt"
    filepath=root_dir/Path(filename) # path + name is given here
    filepath.touch() # crearing this file

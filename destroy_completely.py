# Firstly we change content in the files, using binary values and later we delete this file
from pathlib import Path
dir_for_destruction=Path("pathlib_local_files/data_by_years")

for file in dir_for_destruction.glob("**/*.csv"): # finds all csv files in this dir plus in sub dir to0 
    with open(file,"wb") as csv: # for changing a content of cvs file
        csv.write(b'')
    file.unlink() # for deleting a csv file 

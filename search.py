from pathlib import Path
import re
downloads=Path("/Users/rock/Downloads/")
print(downloads.absolute())
file_count=0
dir_count=0

for file in downloads.rglob("*"):
    
    if file.is_file():
        #file_count+=1
        match_jpg=re.search(r".*\.jpg",file.name) #patter for each line in file variable to search for
        if match_jpg:
            file_count+=1
            print(match_jpg.group())
            print(f"File: {file.name}")
            print(f"the location of this pic: {file.absolute()}")
    else:
        dir_count+=1
        print(f"Directory: {file.name}")
print(f"\nTotal Files: {file_count}\nTotal dirs: {dir_count}")
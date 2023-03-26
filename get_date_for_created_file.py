from pathlib import Path
from datetime import datetime
import re
#command + shift + L => multiple cursor
root=Path("data_by_years")
structure_for_date_and_time="%Y-%m-%d_%H:%M:%S"
stats_edu=root.stat() # some info about file/dir like when it was created/modified etc
original_second_created=stats_edu.st_ctime # getting seconds form 1970 till now for machines
date_created=datetime.fromtimestamp(original_second_created) # converting secodns for humans
date_created_str=date_created.strftime(structure_for_date_and_time) #converting from  <class 'datetime.datetime'> to <class 'str'>  

#Now I can edit the files' names based on when they're created 
files_paths=root.glob("**/*")
for file_path in files_paths:
    if file_path.is_file():
        org_date_str=(datetime.fromtimestamp(file_path.stat().st_ctime)).strftime(structure_for_date_and_time)
        get_curr_name= file_path.stem
        match=re.search(r"_(\w)_?$",get_curr_name) # getting just letter since it original name of the file
        if match:
                get_original_name=match.group(1)
                new_name=org_date_str+"_"+get_original_name+file_path.suffix
        new_filepath=file_path.with_name(new_name) # takes a new name and keeps this file in the same place "with_name" method
        file_path.rename(new_filepath)  

        

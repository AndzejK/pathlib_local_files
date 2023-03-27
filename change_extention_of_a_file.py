# Change the extentions txt and jpg -> csv in 2022/December dir 

from pathlib import Path
root=Path("data_by_years")
dir=Path("2022")
subdir=Path("December")

# The path to dir where I want to change the extentions 
path_to_the_files=root/dir/subdir

# Now I'm going loop through dir to see what I have in that dir
files=path_to_the_files.iterdir()
extentions=['.csv',['mp3']]

#for file in files: 
#    get_stem=file.stem
#    new_extention=get_stem+extentions[0] # the original name and changing extention to .cvs
#    new_file_name=file.with_name(new_extention) # here I construct a name/ext of a file
#    file.rename(new_file_name)

for file in files:
    new_filepath=file.with_suffix(".csv") # with_suffix changes just extention 
    file.rename(new_filepath)
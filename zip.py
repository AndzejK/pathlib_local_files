from pathlib import Path
import zipfile
import datetime

root_dir=Path("pathlib_local_files/data_by_years")
dest_dir=Path('backup')
# I'm gonna zip it up and later on uzip it
get_today_date=str(datetime.date.today())
backup_path = dest_dir / get_today_date # here is a path where we will store this archive plus it name
backup_path.mkdir(exist_ok=True) # create backup directory if it doesn't exist

print(type(backup_path))  #-> <class 'pathlib.PosixPath'>
print(backup_path.as_posix())  #<class 'str'>

# find what is just in this directory!
content_of_root_dir = root_dir.glob("*/")
for dir in content_of_root_dir:
    archive_name=backup_path/(dir.name+".zip")
    # I want to zip each dir separately and copy/move to backup dir
    with zipfile.ZipFile(archive_name,"w") as zf:
        for file_in_directory in dir.glob("*"):
            zf.write(file_in_directory)
        

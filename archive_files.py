from pathlib import Path
import zipfile
import datetime

root_dir=Path("txt_files_from_A_to_Z")
get_today_date=str(datetime.date.today())
archive_path=root_dir/Path(f"archive_{get_today_date}.zip") # here is a path where we will store this archive plus it name
with zipfile.ZipFile(archive_path,"w") as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
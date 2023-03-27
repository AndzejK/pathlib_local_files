from pathlib import Path
import zipfile

#somewhere here zipped files
backup_dir_root=Path('backup')
#where I these files will be unzipped
dest_dir=Path("unzip_files")

for path in backup_dir_root.rglob("*.zip"): # rglob() = glob(**/*)
    with zipfile.ZipFile(path,"r") as zf:
        final_path=dest_dir/ Path(path.stem)
        zf.extractall(path=final_path)



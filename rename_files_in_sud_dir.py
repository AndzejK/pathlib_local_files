from pathlib import Path

# I have files in data_by_years / 2022 / December / a.txt; file a.txt should be renamed 2022-December-a.txt

root=Path('data_by_years')

files_path=root.glob("**/*")
for file_path in files_path:
    if file_path.is_file():
        get_parent_dir=file_path.parts[-3] # Parts it breaks down dirs and files and stored in tuples
        get_child_dir=file_path.parts[-2]
        new_file_name=f"{get_parent_dir}_{get_child_dir}_{file_path.stem}{file_path.suffix}"
        new_file_path=file_path.with_name(new_file_name)
        file_path.rename(new_file_path)
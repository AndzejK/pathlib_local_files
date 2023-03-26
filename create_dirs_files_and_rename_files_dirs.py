
from pathlib import Path
import datetime
import os
import random

# Set variables
root = 'data_by_years'
prefix = ['txt', 'jpg']
current_year = datetime.date.today().year
years = [current_year, current_year - 1]
months = ["December", "November"]

# Creation of folders and files
for year in years:
    for month in months:
        # Create subdirectory
        dict_in_dict = Path(root) / str(year) / month
        os.makedirs(dict_in_dict, exist_ok=True)

        # Generate file names
        existing_files = [f.stem for f in dict_in_dict.glob("*")]
        new_file_names = [chr(i) for i in range(ord('a'), ord('h')+1) if chr(i) not in existing_files]

        # Create files
        for file_name in new_file_names:
            file_x = dict_in_dict / f"{file_name}.{random.choice(prefix)}"
            with open(file_x, "w") as file:
                file.write("Random content")





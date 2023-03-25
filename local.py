# tests - to push to hub I used this command ->  git push -u gith mac
from pathlib import Path
#print (dir(Path)) -> exists(), name(), rename() etc

path_to_file_1=Path("files/file_1.txt")
path_to_file_2=Path("files/file_2.txt")

#print(path_to_file_1.name)
if not path_to_file_2.exists(): # if the file does not exist then create a file
    with open(path_to_file_2,"w") as file:
        (file.write("#2 Random contect "))
print(path_to_file_2.read_text())

#lets find content in the dictionary/folder or path of it
files_dic=Path("files")
fulL_path=(files_dic.resolve()) # with resolve() I can use full path 
#Content/other files in this dictionary
content_of_files=files_dic.iterdir()
for item in content_of_files:
    print (f"Path: {item}; Type: {type(item)}")
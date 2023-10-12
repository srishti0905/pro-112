import os
import shutil
from_dir="C:/Users/vipin kumar/Downloads"
to_dir="C:/Users/vipin kumar/OneDrive/Desktop/whj/111-pro"
listOfFiles = os.listdir(from_dir)
print(listOfFiles)
for file_name in listOfFiles:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext=='':
        continue
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + "Document_Files" 
    path3 = to_dir + '/' + "Document_Files" + '/' + file_name 
    if os.path.exists(path2):
        print("moving, to your directary"+file_name+"....")
        shutil.move(path1,path3)
    else:
        os.mkdir(path2)
        print("moving, to your directary"+file_name+"....")
        shutil.move(path1,path3)
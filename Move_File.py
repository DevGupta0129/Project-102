import os
import shutil

from_dir ="Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)


for i in list_of_files:
    file_name , extension = os.path.splitext(i)

    if(extension==""):
        continue
    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + i
        
        if(os.path.exists(path2)):
            print("Moving the file",i)
            shutil.move(path1,path3)
        else:
            print("Folder doesn't exist")
            os.mkdir(path2)
            print("Folder created.........")
            print("Moving the file",i) 
            shutil.move(path1,path3)
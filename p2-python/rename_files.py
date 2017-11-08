import os 
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"F:\udactiy\p2-python\rename_file\prank")
    print(file_list)
    saved_path = os.getcwd()
    print saved_path
    os.chdir(r"F:\udactiy\p2-python\rename_file\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,'0123456789'))
    os.chdir(saved_path)
rename_files()
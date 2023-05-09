# Christopher Lama
import subprocess
import traceback
import os
import inquirer as iq

try:
    final_file_name = input("NAME OF EXE: ")
    choice = input("COMPILE ALL OR SOME (a/s) : ")
    pwd_dir = os.getcwd() # get current working directory: https://stackoverflow.com/questions/37427683/python-search-for-a-file-in-current-directory-and-all-its-parents
    cpp_file_list = []

    if choice.lower() == "all" or choice.lower() == "a":

        for files in os.listdir(pwd_dir):
            if files.endswith(".cpp") or files.endswith(".h"):
                cpp_file_list.append(os.path.join(pwd_dir, files))
                print(cpp_file_list)


        command = ["g++"] + cpp_file_list + ["-o", os.path.join(pwd_dir, final_file_name + ".exe")]
        subprocess.run(command,shell=False)
        input("Successful compiling. \nPress any key to exit ...")

    elif choice.lower() == "some" or choice.lower() == "s":

            file_list = []
            for file in os.listdir(os.getcwd()):
                if file.endswith(".cpp") or file.endswith(".h"):
                    file_list.append(os.path.abspath(os.path.join(pwd_dir, file)))

            questions = [iq.Checkbox('file',
                                     message="Choose file path(s): ",
                                     choices=file_list), ]

            answers = iq.prompt(questions)
            selected_files = answers['file']
            files_string = " ".join(selected_files)
            command = ["g++"] + selected_files + ["-o", os.path.join(pwd_dir, final_file_name + ".exe")]
            subprocess.run(command, shell=False)
            input("Successful compiling.\nPress any key to exit ...")



except:
    traceback.print_exc()
    input("Press any key to exit ...")


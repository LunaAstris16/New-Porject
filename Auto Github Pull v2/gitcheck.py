import os
import subprocess
from functions import *

"""
This is used to git the latest github instance of the chosen repo
it then checks that with the current one
if it has an update it will pull the latest version and update the current 
"""


def up_to_date_check(testing_folder_index: int, home_folder: str) -> bool:
    folder_check(home_folder) # this just routs back to the "home" directory
    ls_output: list[str] = os.popen("ls").read().split("\n")
    os.chdir(ls_output[testing_folder_index])
    subprocess.run(["git", "fetch", "origin"]) # this is where the git check happens
    output: str = os.popen("git status").read()
    folder_check(home_folder)
    subprocess.run(["touch", "output.txt"])
    with open("output.txt", "w") as github_out:
        github_out.write(output)
    list_text: list[str] = [line.strip() for line in output.split("\n")]
    git_status = list_text[1].split()
    if git_status[3] == "behind": # come fix this later you can yeet this line of code
        os.chdir(ls_output[testing_folder_index])
        subprocess.run(["git", "pull"])
        folder_check(home_folder)
        os.remove("output.txt")
        return True 
    os.remove("output.txt")
    return False
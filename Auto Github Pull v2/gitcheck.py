import os
import subprocess
from functions import *

"""
This is used to git the latest github instance of the chosen repo
it then checks that with the current one
if it has an update it will pull the latest version and update the current 
"""

def up_to_date(filename) -> bool:
    
    output = os.popen("git status").read().split("\n")[0].split(" ")
    
    return_value = "Failed"
    
    if output[0] == "behind":
        subprocess.run(["git", "pull"])
        return "Off"
    elif output[0] == '':
        os.chdir(filename)
        return_value = up_to_date(filename)
    elif output[0] == 'On':
        return "On"
    
    return return_value
    
#print(up_to_date("GitHub-Pull-V2"))

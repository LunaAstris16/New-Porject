import os
import subprocess
import threading
from functions import *
from gitcheck import *
import time

"""
This intilizes a run thread
it starts the object and then 
"""

class runThread:

    def __init__(self, runfile_name: str, location_folder: str) -> None:
        self.runfile_name: str = runfile_name
        self.location_folder: str = location_folder
        self.home_folder: str = os.getcwd()
        self.status = False
        self.testing_folder_index: int = os.popen("ls").read().split("\n").index(location_folder)
        self.run_thread = threading.Thread(target=self.run_file, daemon=False)
        self.process = None
        self.ls_output: list[str] = os.popen("ls").read().split("\n")
      
    def run_file(self):
        folder_check(self.home_folder)
        os.chdir(self.location_folder)
        self.process = subprocess.Popen(["python", self.runfile_name])
        os.chdir("..")
        self.status = True

    def updater(self): 
        while True:
            folder_check(self.home_folder)
            os.chdir(self.ls_output[self.testing_folder_index])
            changed_branch: bool = up_to_date_check(self.testing_folder_index, self.home_folder)
            if changed_branch:
                print("Your Repository was updated Auto run Started")
                self.runthreadob.restart_process()
            else:
                print("Your repository is up to date")
                time.sleep(10)
                print() # newline

    def start_run_thread(self):
        self.run_thread.start()
        self.status = True

    def stop_process(self):
        self.status = False
        if self.process is not None:
            self.process.terminate()

    def restart_process(self):
        if self.process is not None:
            self.process.terminate()
        self.run_thread.start()
    
    def status_checker(self):
        return self.status

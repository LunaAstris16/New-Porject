import os
import string
import subprocess
import time
import threading
import functions
import runthread

"""
This is whats going to be usef for all of the colotrolling the thread objects
"""
class operation_object:

    """
        This is the object that runs and store all the data and ability to control each thread
        You can do lots of different things with this object
        here's a list of some of the things that you can do
        -Initial Creation
            -Do the clone request
            -Start the function
        -Check the uptime
            -reset time function
        -check the last time that that there was a git pull
        -check the status 
    """

    def __init__(self, github_url: str, location_folder: str, update_period: int, run_file_name: str) -> None:
        self.github_url = github_url
        self.folder_name = location_folder
        self.update_period = update_period
        self.global_time = 0
        self.run_file_name = run_file_name
        self.time_started = time.localtime()
        self.run_thread_object = runthread.runThread(self.folder_name, run_file_name)

    def start_runthread(self) -> bool:
        #make sure that we are in the base folder
        #Get the repository from git hub
        #then cd into that folder and start the run thread
        functions.folder_check()
        subprocess.run(["git", "clone", self.github_url])
        subprocess.run(["cd", self.folder_name])
        self.run_thread_object.start_run_thread()
        pass
    

    def getup_time(self):
        return self.time_started

    def getpull_time(self) -> int:
        pass

    def status_check(self) -> string: #This is a function that checks to see if the procsess is running or not
        if self.run_thread_object.status_checker() == True:
            return "The process is online"
        return "The process is ofline"

    def rest_time(self) -> None:
        self.time_started = time.localtime()
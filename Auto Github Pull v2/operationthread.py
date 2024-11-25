import os
import string
import subprocess
import time
import threading
import functions

class operation_object:

    def __init__(self, github_url: str, location_folder: str, update_period: int, run_file_name: str) -> None:
        self.github_url = github_url
        self.folder_name = location_folder
        self.update_period = update_period
        self.global_time = 0
        self.run_file_name = run_file_name
        self.time_started = time.localtime()

    def start_runthread(self) -> bool:
        

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
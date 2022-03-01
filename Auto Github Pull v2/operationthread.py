import os
import subprocess

"""
This is whats going to be usef for all of the colotrolling the thread objects
"""
class operation_object:

    """
        This is the object that runs and store all the data and ability to control each thread
        You can do lots of different things with this object
        here's a list of some of the things that you can do
        -Check the uptime
        -check the last time that that there was a git pull
        -check the status 
    """

    def __init__(self, github_url: str, location_folder: str, update_period: int) -> None:
        self.github_url = github_url
        self.folder_name = location_folder
        self.update_period = update_period

    def getup_time(self):
        pass

    def getpull_time(self):
        pass

    def status_check(self):
        pass

"""
This is where all of the user interaction will go just to process all of the "front end"

This file is going to have a lot of the main functonality and controlling of the processes

The User needs to create a Jason file that has all of the:
    github links 
    process names 
    location folder 
    update checker period

-The Click Library is going to be used for the user to be able to have a custom command
    -The command will be:
        github-checker --Jasonfile Name

Then we are going to process through the jason file and start operations for every process that the user
described in the jason file

Then create then start the user terrminal process and run that on it's own thread

"""

import click
@click.command()
@click.option('--jasonfile', prompt='What is the name of the Jason file', help='This is where you place the name of the jason file')
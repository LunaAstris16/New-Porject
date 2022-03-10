import os

def folder_check(home_folder: str) -> bool:
    ls_output: list[str] = os.popen("ls").read().split("\n")
    """
    Checks the folder to make sure it's in the home directory.
    """
    current_folder: str = os.getcwd()
    if home_folder == current_folder:#checks to see if in the right folder
        return True
    for ls_dir in ls_output:
        if ls_dir == home_folder: # if the home folder is found then it cds into that
            os.chdir(home_folder)
            return True 
    os.chdir("..")
    current_folder: str = os.getcwd() # checks the parent directory to see if that is the home directory
    if home_folder == current_folder:
        return True
    return False # False is better than None honestly even if this latter also works

def folder_name_finder(github_url: str) -> str:
    """
    Finds the folder name of the clone folder
    """
    # git_folder contains all the list element except the last one
    # which is stored in git_file
    *git_user_path, git_repository = github_url.split("/")
    return git_repository.removesuffix(".git")
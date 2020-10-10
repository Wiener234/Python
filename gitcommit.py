import os
import sys
from github import Github


def create():

    folderName = str(sys.argv[1])
    commitName = str(sys.argv[2])
    path = 'E:/test/'  # add projects dirctory to the env vars
    token = 'bfa0b236b3b1ed923a8865e0be15659f14235dba'  # add github token to the env vars

    g = Github(token)




    os.chdir(path + str(folderName))
    os.system('git add .')
    os.system(f'git commit -m "{commitName} commit"')
    os.system('git push -u origin master')
    print("Succesfully comited to repository {}" .format(folderName))


if __name__ == "__main__":
    create()
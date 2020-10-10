import os
import sys
from github import Github


def create():

    folderName = str(sys.argv[1])
    path = 'E:/test/'  # add projects dirctory to the env vars
    token = 'bfa0b236b3b1ed923a8865e0be15659f14235dba'  # add github token to the env vars

    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(folderName)

    # print(folderName)
    os.mkdir(path + str(folderName))
    os.chdir(path + str(folderName))
    os.system(f'echo "# {folderName}" >> README.md')
    os.system('git init')
    os.system(f'git remote add origin https://github.com/Wiener234/{folderName}.git')
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
    os.system('git push -u origin master')
    os.system('code .')
    print("Succesfully created repository {}" .format(folderName) + "and started vs code")


if __name__ == "__main__":
    create()



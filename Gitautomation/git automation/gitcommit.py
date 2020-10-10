import os
import sys
from github import Github
from dotenv import load_dotenv, find_dotenv


def create():

    load_dotenv()
    path = os.getenv("FILEPATH") 
    token = os.getenv("TOKEN")

    folderName = str(sys.argv[1])
    commitName = str(sys.argv[2])
    

    g = Github(token)




    os.chdir(path + str(folderName))
    os.system('git add .')
    os.system(f'git commit -m "{commitName} commit"')
    os.system('git push -u origin master')
    print("Succesfully comited to repository {}" .format(folderName))


if __name__ == "__main__":
    create()
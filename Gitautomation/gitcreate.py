import os
import sys
from github import Github
from dotenv import load_dotenv, find_dotenv






def create():
    # os.path.join(project_folder, '.env')
    # project_folder = os.path.expanduser(r'C:\Users\nilsb\Desktop\Custom_CMD_commands')

    load_dotenv()

    folderName = str(sys.argv[1])
    path = os.getenv("FILEPATH")  # add projects dirctory to the env vars
    token = os.getenv("TOKEN")  # add github token to the env vars 
    username = os.getenv("USERNAME")

    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(folderName)

    print(path)
    os.mkdir(path + str(folderName))
    os.chdir(path + str(folderName))
    os.system(f'echo "# {folderName}" >> README.md')
    os.system('git init')
    os.system(f'git remote add origin https://github.com/{username}/{folderName}.git')
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
    os.system('git push -u origin master')
    os.system('code .')
    print("Succesfully created repository {}" .format(folderName) + "and started vs code")


if __name__ == "__main__":
    create()



from cmd import Cmd
import os
import subprocess
# os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git






class MyPrompt(Cmd):

    prompt = '>>>'

    def do_add(self, inputpath):
        path = 'E:/save/Desktop/Visual Studio Code Projekts/' + inputpath
        try:

            os.mkdir(path)
            git.Repo.init(path)
            with open(os.path.join(path, 'README.md'), 'w'):
                pass
            subprocess.run("git add README.md")

        except:
            print("Failed to create folder at: " + path)

    def do_cd(self, inp):
        path = 'E:/save/Desktop/Visual Studio Code Projekts/'
        global inppath
        try:
            inppath = path + inp
        except:
            print("Cant find directroy")

    def do_add_file(self, inp):
        path = 'E:/save/Desktop/Visual Studio Code Projekts/'
        with open(os.path.join(inppath, inp), "w"):
            pass








MyPrompt().cmdloop()

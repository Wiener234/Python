import os 
import sys
from dotenv import load_dotenv

def open():
    load_dotenv()

    path = os.getenv("FILEPATH")

    foldername = str(sys.argv[1])

    os.chdir(path + str(foldername))
    os.system('code .')


if __name__ == "__main__":
    open()
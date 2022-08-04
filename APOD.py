
from sys import platform
import os
#######################################
# Insert other modules to import here
#######################################

import requests

def clearConsole():
    if os.name in ('nt','dos'):
        command = 'cls'
    else:
        command = 'clear'

    os.system(command)

# print(platform.system)


def main():

    if platform == "darwin":
        os_platform = "Mac"
        clearConsole()
    else:
        os_platform = "Windows"
        clearConsole()
        print("Hello")
        input("Press any key to exit")


################# Main Processing Section ##############################

if __name__ == '__main__':
    main 

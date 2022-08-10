
from sys import platform
import os
#######################################
# Insert other modules to import here
#######################################

import requests
import json
from datetime import datetime
import urllib.request
import sys
import pandas as pd
import os

def clearConsole():
    if os.name in ('nt','dos'):
        command = 'cls'
    else:
        command = 'clear'

    os.system(command)

    #print(os.getcwd())

def main():

    rover = sys.argv[1]
    camera = sys.argv[2]
    earth_date = sys.argv[3]

    currentDirectory = os.getcwd()

    if platform == "darwin":
        os_platform = "Mac"
        excelFile = currentDirectory + "/" + rover + ".xlsx"
        baseImageFolder = "/Users/ron/OneDrive/Photos/NASA/"
        clearConsole()
    else:
        os_platform = "Windows"
        excelFile = currentDirectory + "\\" + rover + ".xlsx"
        baseImageFolder = "C:\\Users\\rowle\\OneDrive\\Photos\\NASA\\"
        clearConsole()


def buildFolderStructure():
    print('')


################# Main Processing Section ##############################

if __name__ == '__main__':
    start_date = '2022-07-10'
    end_date = '2022-07-20'
    main()


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

    api_key = 'CAejpD9hOfWhaGxZyv2p6bS9A7HmBP1Sf53Vp8yi'

    if platform == "darwin":
        os_platform = "Mac"
        excelFile = currentDirectory + "/" + rover + ".xlsx"
        baseImageFolder = "/Users/ron/OneDrive/Photos/NASA/"
        roverFolder = baseImageFolder + rover + "/"
        roverDateFolder = roverFolder + earth_date + "/"
        roverCameraFolder = roverDateFolder + camera + "/"

        if not os.path.exists(roverDateFolder):
            os.makedirs(roverDateFolder)

        if not os.path.exists(roverCameraFolder):
            os.makedirs(roverCameraFolder)

        clearConsole()
    else:
        os_platform = "Windows"
        excelFile = currentDirectory + "\\" + rover + ".xlsx"
        baseImageFolder = "C:\\Users\\rowle\\OneDrive\\Photos\\NASA\\"
        roverFolder = baseImageFolder + rover + "\\"
        roverDateFolder = roverFolder + earth_date + "\\"
        roverCameraFolder = roverDateFolder + camera + "\\"

        if not os.path.exists(roverDateFolder):
            os.makedirs(roverDateFolder)

        if not os.path.exists(roverCameraFolder):
            os.makedirs(roverCameraFolder)

        clearConsole()

    print('Rover: {0}', rover)
    print('Camera: {0}', camera)
    print('EarthDate: {0}', earth_date)

    data = getAPIData(rover, earth_date, camera, api_key)

    print(data)

def getAPIData(rover, earth_date, camera, api_key):
    params = {'earth_date': earth_date, 'camera': camera, 'api_key': api_key}   

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/' + rover + '/photos?'

    print(url)

    data = requests.get(url, params=params)

    data = json.loads(data.text)

    return data 


################# Main Processing Section ##############################

if __name__ == '__main__':
    main()

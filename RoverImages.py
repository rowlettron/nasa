#python RoverImages.py "curiosity" "NAVCAM" "2015-08-04"

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
from configparser import ConfigParser

def get_api_key():
    config = ConfigParser()
    config.read("nasa.ini")
    return config["nasa"]["api_key"]

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

    api_key = get_api_key()

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

    print('Rover: {0}'.format(rover))
    print('Camera: {0}'.format(camera))
    print('EarthDate: {0}'.format(earth_date))

    data = getAPIData(rover, earth_date, camera, api_key)

    parseAPIData(data, roverCameraFolder)

def getAPIData(rover, earth_date, camera, api_key):
    params = {'earth_date': earth_date, 'camera': camera, 'api_key': api_key}   

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/' + rover + '/photos?'

    #print(url)

    response = requests.get(url, params=params)

    jsonobject = json.loads(response.text)

    return jsonobject  

def parseAPIData(jsonobject, roverCameraFolder):
    #print("Parsing api data")

    #print(type(jsonobject))
    #print(jsonobject)

    #data = jsonobject
    #print(type(data))


    for item in jsonobject['photos']:
        id = item['id']
        sol = item["sol"]
        img_src = item['img_src']

        print("id: {0}".format(id))
        print("sol: {0}".format(sol))
        print("img_src: {0}".format(img_src))

        imageName = roverCameraFolder + str(id) + '.jpg'
        urllib.request.urlretrieve(img_src, imageName)

def saveImageFile():
    print('')



################# Main Processing Section ##############################

if __name__ == '__main__':
    main()

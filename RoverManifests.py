
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

def main():

    rover = sys.argv[1]
    currentDirectory = os.getcwd()

    if platform == "darwin":
        os_platform = "Mac"
        excelFile = currentDirectory + "/" + rover + ".xlsx"
        clearConsole()
    else:
        os_platform = "Windows"
        excelFile = currentDirectory + "\\" + rover + ".xlsx"
        clearConsole()



    #print(rover)

    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/" + rover + "/?api_key=CAejpD9hOfWhaGxZyv2p6bS9A7HmBP1Sf53Vp8yi"
    print(url)
    #weatherobject = json.loads(data.decode("utf-8"))

    manifest = getAPIData(url)

    photolist = manifest['photo_manifest']['photos']



    df = pd.json_normalize(manifest)
    df.rename(columns = {'photo_manifest.name':'lander_name',
                         'photo_manifest.landing_date':'landing_date',
                         'photo_manifest.launch_date':'launch_date',
                         'photo_manifest.status':'status',
                         'photo_manifest.max_sol':'max_sol',
                         'photo_manifest.max_date':'max_date',
                         'photo_manifest.total_photos':'total_photos',
                         'photo_manifest.photos':'photos'}, inplace=True)

    df.drop(columns=['photos'], inplace=True)

    df1 = pd.DataFrame(photolist)
    with pd.ExcelWriter(excelFile, mode="a", engine="openpyxl") as writer:

        df.to_excel(writer, sheet_name="Lander")
        df1.to_excel(writer, sheet_name="Details")


def clearConsole():
    if os.name in ('nt','dos'):
        command = 'cls'
    else:
        command = 'clear'

    os.system(command)

def getAPIData(url):
    print('')

    response = requests.get(url)

    jsonobject = response.json()

    return jsonobject

################# Main Processing Section ##############################

if __name__ == '__main__':
    start_date = '2022-07-10'
    end_date = '2022-07-20'
    main()

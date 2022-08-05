
from sys import platform
import os
#######################################
# Insert other modules to import here
#######################################

import requests
import json
from datetime import datetime
import urllib.request

def clearConsole():
    if os.name in ('nt','dos'):
        command = 'cls'
    else:
        command = 'clear'

    os.system(command)

    #print(os.getcwd())


def main():

    if platform == "darwin":
        os_platform = "Mac"
        clearConsole()
    else:
        os_platform = "Windows"
        clearConsole()
        #print("Hello")
        #input("Press enter to exit")

    daysDiff = calculateDays(start_date, end_date)
    jsonobject = getAPIData(start_date, end_date)

    extractData(jsonobject, daysDiff)

def calculateDays(start_date, end_date):
    date_format = "%Y-%m-%d"
    d0 = datetime.strptime(start_date, date_format)
    d1 = datetime.strptime(end_date, date_format)

    delta = d1 - d0
    days = delta.days

    return days

def getAPIData(start_date, end_date):
    print('')

    #start_date = "2022-07-10"
    #end_date = "2022-07-20"

    api_key = "CAejpD9hOfWhaGxZyv2p6bS9A7HmBP1Sf53Vp8yi"
    url = "https://api.nasa.gov/planetary/apod"

    # valid parameters are date, start_date, end_date, count, thumbs, api_key

    params = {"start_date": start_date, "end_date": end_date, "api_key": api_key}

    response = requests.get(url, params=params)
    #print(response)

    jsonobject = response.json()

    return jsonobject

def extractData(dataobject, days):
    topindex = days

    currentDirectory = os.getcwd()
    imageDirectory = currentDirectory + "\\images\\"

    for index in range(topindex):
        print(index)
        date = dataobject[index]["date"]
        explanation = dataobject[index]["explanation"]
        hdurl = dataobject[index]["hdurl"]
        media_type = dataobject[index]["media_type"]
        service_version = dataobject[index]["service_version"]
        title = dataobject[index]["title"]
        sdurl = dataobject[index]["url"]

        imageName = imageDirectory + title + ".jpg"
        urllib.request.urlretrieve(hdurl, imageName)

        print("Date: {0}".format(date))
        print("Explanation: {0}".format(explanation))
        print("HDURL: {0}".format(hdurl))
        print("Media Type: {0}".format(media_type))
        print("Service Version: {0}".format(service_version))
        print("Title: {0}".format(title))
        print("URL: {0}".format(sdurl))
        print("")
        print("###################################################################################")
        print("")


################# Main Processing Section ##############################

if __name__ == '__main__':
    start_date = '2022-07-10'
    end_date = '2022-07-20'
    main()

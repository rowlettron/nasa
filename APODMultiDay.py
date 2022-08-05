
from sys import platform
import os
#######################################
# Insert other modules to import here
#######################################

import requests
import json 

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
        #print("Hello")
        #input("Press enter to exit")

    jsonobject = getAPIData() 

    extractData(jsonobject)

def getAPIData():
    print('')

    start_date = "2022-07-10"
    end_date = "2022-07-20"

    api_key = "CAejpD9hOfWhaGxZyv2p6bS9A7HmBP1Sf53Vp8yi"
    url = "https://api.nasa.gov/planetary/apod"

    # valid parameters are date, start_date, end_date, count, thumbs, api_key

    params = {"start_date": start_date, "end_date": end_date, "api_key": api_key}

    response = requests.get(url, params=params)
    #print(response)

    jsonobject = response.json() 

    return jsonobject

def extractData(dataobject):

    #for item in dataobject[]:
    #    copyright = item["copyright"]

    copyright = dataobject[0]["copyright"]
    #date = dataobject["date"]
    #explanation = dataobject["explanation"]
    #hdurl = dataobject["hdurl"]
    #media_type = dataobject["media_type"]
    #service_version = dataobject["service_version"]
    #title = dataobject["title"]
    #sdurl = dataobject["url"]

    print("Copyright: {0}".format(copyright))

    #print("Date: {0}".format(date))
    #print("Explanation: {0}".format(explanation))
    #print("HDURL: {0}".format(hdurl))
    #print("Media Type: {0}".format(media_type))
    #print("Service Version: {0}".format(service_version))
    #print("Title: {0}".format(title))
    #print("URL: {0}".format(sdurl))


################# Main Processing Section ##############################

if __name__ == '__main__':
    main()


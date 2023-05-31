from constants import Constants
import requests
import os
import urllib.request
import json
import bisect

class DownloadMods:

    def getJarFiles(arg, headers):
        links=[]
        with open(arg,'r', encoding='utf8') as f:
            data= json.load(f)
            for entry in data:
                modId = str(entry["projectID"])
                fileId = str(entry["fileID"])
                url = Constants.apiEndpoint+'/v1/mods/'+modId+'/files/'+fileId
                response = requests.get(url, headers=headers)
                response = response.json()
                if(response["data"]["downloadUrl"] != None):
                    jarLink = str(response["data"]["downloadUrl"]).replace(" ", "%20")
                    bisect.insort_left(links, jarLink)
        f.close()
        with open('jarLinks.txt', 'w') as f:
            f.write('\n'.join(links))
            
    
    def getJarLinks(arg):
        with open(arg, 'r', encoding='utf8') as f:
            data = json.load(f)
            with requests.Session() as session:
                for entry in data:
                    url = Constants.url + str(entry["projectID"]) + "/" + str(entry["fileID"])
                    try:
                        response = session.get(url)
                        response.raise_for_status()
                        response = response.text
                        jarFile = response.splitlines()[-1].strip("Found:")
                        print(f"JarFile link ----> {jarFile}")
                        jarFile = jarFile.strip().replace(' ', '%20')
                        if(jarFile != "Error"):
                            with open("jarLinks.txt", 'a') as f:                                
                                f.write(jarFile + '\n')
                    except requests.RequestException as e:
                        print(f"Failed to fetch {url}: {e}")
    
    def testLinks(arg):
        f = open(arg, 'r')
        lines = f.readlines()
        with requests.Session() as session:
            for url in lines:
                try:
                    response = session.get(url)
                    response.raise_for_status()
                except requests.RequestException as e:
                    print(f"URL FAILED---> {url}: {e}")


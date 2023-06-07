import json
import os
from downloadMods import DownloadMods
from constants import Constants
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("API_KEY")

GETheaders = {
  'Accept': 'application/json',
  'x-api-key': apiKey
}

POSTheaders = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-api-key': apiKey
}

if(os.path.exists(Constants.mainfest) == False):
    with open(Constants.mainfest, 'r', encoding="utf8") as f:
        data = json.load(f)

if(os.path.exists(Constants.mods) == False):
    with open(Constants.mods,'w', encoding="utf8") as f:
        json.dump(data["files"],f)
        
#DownloadMods.getJarFiles(Constants.mods, GETheaders)
DownloadMods.test(Constants.mods, POSTheaders)
#DownloadMods.getJarLinks(Constants.mods)
#DownloadMods.testLinks("jarLinks.txt")
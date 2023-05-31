import json
import os
from downloadMods import DownloadMods
from constants import Constants
from dotenv import load_dotenv

load_dotenv()

headers = {
  'Accept': 'application/json',
  'x-api-key': os.getenv("API_KEY")
}
if(os.path.exists(Constants.mainfest) == False):
    with open(Constants.mainfest, 'r', encoding="utf8") as f:
        data = json.load(f)

if(os.path.exists(Constants.mods) == False):
    with open(Constants.mods,'w', encoding="utf8") as f:
        json.dump(data["files"],f)
        
DownloadMods.getJarFiles(Constants.mods, headers)
#DownloadMods.getJarLinks(Constants.mods)
#DownloadMods.testLinks("jarLinks.txt")
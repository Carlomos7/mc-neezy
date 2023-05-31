import json
import os
from downloadMods import DownloadMods
from constants import Constants

if(os.path.exists(Constants.mainfest) == False):
    with open(Constants.mainfest, 'r', encoding="utf8") as f:
        data = json.load(f)

if(os.path.exists(Constants.mods) == False):
    with open(Constants.mods,'w', encoding="utf8") as f:
        json.dump(data["files"],f)

DownloadMods.getJarFiles(Constants.mods)
#DownloadMods.getJarLinks(Constants.mods)
#DownloadMods.testLinks("jarLinks.txt")
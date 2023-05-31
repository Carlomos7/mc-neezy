import os
from dotenv import load_dotenv


class Constants:
    load_dotenv('.env')
    url = "https://www.cursemaven.com/test/"
    apiEndpoint = "https://api.curseforge.com"
    version = "1.5.0"
    mainfest = "python\json\manifest.json"
    mods = "python\json\mods.json"
    

import os
import json

class BuildJson:

    def modIdJSON(modIds):
        with open(modIds, 'w') as f:
            json.dump(data, f)


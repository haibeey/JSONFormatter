"""

USAGE:
from JSONFormatter.JSONFormatter import JSONFormatter
jf=JSONFormatter(jsonString)
formattedJson=jf.parse()
NOTE: It create a new text file called data

EXPECTED USAGE:user should override class and call self._parse(spaceLenght) for result
"""

import json

class error(Exception):
    pass

class JSONFormatter(object):
    def __init__(self,Json):
        self.json=Json
        self.JSON=json.loads(self.json)
    def newTab(self,count):
        return " "*count
        
    def _parse(self,data,spaceLenght):
        res=""
        if isinstance(data,dict):
            res+="{\n"
            for key in data:
                res+=self.newTab(spaceLenght+1)+key+":"+self._parse(data[key],spaceLenght+1)
            res+="\n}"
        elif isinstance(data,list):
            res+="[\n"
            for item in data:
                res+=self.newTab(spaceLenght+1)+self._parse(item,spaceLenght+1)
            res+=self.newTab(spaceLenght+1)+"]\n"
        elif isinstance(data,str):
            res+=self.newTab(spaceLenght+1)+data+"\n"
        else:
            res+=self.newTab(spaceLenght+1)+str(data)+"\n"
        return res

    def parse(self):
        return (self._parse(self.JSON,0))
        


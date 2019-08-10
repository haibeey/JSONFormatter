"""

USAGE:
from JSONFormatter.JSONFormatter import JSONFormatter
jf=JSONFormatter(jsonString)
formattedJson=jf.parse()
NOTE: It create a new text file called data

EXPECTED USAGE:user should override class and call self._parse(spaceLenght) for result
"""

import json
import argparse
import sys



class error(Exception):
    pass

class JSONFormatter(object):
    def __init__(self,Json):
        self.json=Json
        if not Json:
            print("No data")
            exit()
        self.JSON=json.loads(self.json)
    def newTab(self,count):
        return " "*count
    def _comma(self,l):
        return "," if l>0 else ""
    def _key(self,word):
        return '"'+word+'"'

    def _parse(self,data,spaceLenght,lendata):
    
        res=""
        if isinstance(data,dict):
            res+=self.newTab(spaceLenght+1)+"{\n"
            lentd=len(data)
            for key in data:
                lentd=lentd-1
                res+=self._key(key)+":"\
                     +self._parse(data[key],spaceLenght+1,len(data))\
                     +self._comma(lentd)
            res+=self.newTab(spaceLenght+1)+"}\n"

        elif isinstance(data,list):
            res+=self.newTab(spaceLenght+1)+"[\n"
            lentd=len(data)
            for item in data:
                lentd=lentd-1
                res+=self._parse(item,spaceLenght+1,len(data))\
                     +self._comma(lentd)
            res+=self.newTab(spaceLenght+1)+"]\n"

        elif isinstance(data,str):
            res+=self.newTab(spaceLenght+1)\
               +data+" "
        else:
            res+=self.newTab(spaceLenght+1)\
                +str(data)+" "
        return res

    def parse(self):
        return self._parse(self.JSON,0,len(self.JSON)-1)
        


def readAndFormatJsonfile(path):
    try:
        with open(path) as f:
            jf=JSONFormatter(f.read())
        with open(path,"w") as f:
            f.write(jf.parse())
    except FileNotFoundError:
        sys.stdout.write("can't read file\n")
        return ""

def readAndFormatJsonfromStdin():
    try:
        return JSONFormatter(sys.stdin.read()).parse()
    except Exception:
        sys.stdout.write("could not parse data\n")
        return ""

def sentToStdout(fjson):
    sys.stdout.write(fjson)

parser = argparse.ArgumentParser(description='format json files and json data')
parser.add_argument('-f', type=str,help='read from file')

args = parser.parse_args()

readAndFormatJsonfile(args.f)




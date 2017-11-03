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
        



jj=JSONFormatter('{"RAW":{"ETH":{"BTC":{"TYPE":"5","MARKET":"CCCAGG","FROMSYMBOL":"ETH","TOSYMBOL":"BTC","FLAGS":"4","PRICE":0.04267,"LASTUPDATE":1509751124,"LASTVOLUME":0.4,"LASTVOLUMETO":0.017092,"LASTTRADEID":"1769922","VOLUMEDAY":657878.6049690798,"VOLUMEDAYTO":26962.374580809075,"VOLUME24HOUR":649710.1751369004,"VOLUME24HOURTO":26637.795067563067,"OPENDAY":0.04047,"HIGHDAY":0.04336,"LOWDAY":0.03936,"OPEN24HOUR":0.04049,"HIGH24HOUR":0.04352,"LOW24HOUR":0.03929,"LASTMARKET":"Coinbase","CHANGE24HOUR":0.0021800000000000014,"CHANGEPCT24HOUR":5.384045443319342,"CHANGEDAY":0.0022000000000000006,"CHANGEPCTDAY":5.436125525080308,"SUPPLY":95505062.374,"MKTCAP":4075201.0114985798,"TOTALVOLUME24H":1625055.8199134402,"TOTALVOLUME24HTO":68255.79373017802}}},"DISPLAY":{"ETH":{"BTC":{"FROMSYMBOL":"Ξ","TOSYMBOL":"Ƀ","MARKET":"CryptoCompare Index","PRICE":"Ƀ 0.04267","LASTUPDATE":"Just now","LASTVOLUME":"Ξ 0.4000","LASTVOLUMETO":"Ƀ 0.01709","LASTTRADEID":"1769922","VOLUMEDAY":"Ξ 657,878.6","VOLUMEDAYTO":"Ƀ 26,962.4","VOLUME24HOUR":"Ξ 649,710.2","VOLUME24HOURTO":"Ƀ 26,637.8","OPENDAY":"Ƀ 0.04047","HIGHDAY":"Ƀ 0.04336","LOWDAY":"Ƀ 0.03936","OPEN24HOUR":"Ƀ 0.04049","HIGH24HOUR":"Ƀ 0.04352","LOW24HOUR":"Ƀ 0.03929","LASTMARKET":"Coinbase","CHANGE24HOUR":"Ƀ 0.0022","CHANGEPCT24HOUR":"5.38","CHANGEDAY":"Ƀ 0.0022","CHANGEPCTDAY":"5.44","SUPPLY":"Ξ 95,505,062.4","MKTCAP":"Ƀ 4,075.20 K","TOTALVOLUME24H":"Ξ 1,625.06 K","TOTALVOLUME24HTO":"Ƀ 68.26 K"}}}}')
print(jj.parse())

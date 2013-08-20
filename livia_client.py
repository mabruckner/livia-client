import urllib.request
import urllib.parse
import json
import time

class logger():
    url=None
    number=None
    datatype=None
    def __init__(self,url,datatype):
        self.url=url
        response=urllib.request.urlopen(url,data=urllib.parse.urlencode({"datatype":datatype}).encode())
        number = int(response.read())
        #connect and get id here

    def log(self,data,timestamp=None):
        if timestamp is None :
            timestamp = int(time.time())
        outdata = {"logger":self.number,"data":data,"timestamp":timestamp}
        outstring = json.dumps(outdata)
        urllib.request.urlopen(self.url,data=urllib.parse.urlencode({"entry":outstring}).encode())

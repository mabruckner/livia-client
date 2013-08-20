import urllib.request
import urllib.parse
import json
import time

class logger():
    def __init__(self,url,datatype):
        self.url = url
        self.response = urllib.request.urlopen(url,data=urllib.parse.urlencode({"datatype":datatype}).encode())
        self.number = int(response.read())
        #connect and get id here
        pass

    def log(self,data,datatype="",timestamp=None):
        if timestamp is None :
            timestamp = int(time.time())
        outdata = {"logger":self.number,"datatype":datatype,data":data,"timestamp":timestamp}
        outstring = json.dumps(outdata)
        urllib.request.urlopen(self.url,data=urllib.parse.urlencode({"entry":outstring}).encode())

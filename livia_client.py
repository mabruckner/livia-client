import urllib.request
import urllib.parse
import json
import time

class logger():
    def __init__(self,url):
        self.url = url
        response = urllib.request.urlopen(url,data=urllib.parse.urlencode({"authentication":""}).encode())
        self.number = 5
        #connect and get id here
        pass

    def log(self,data,timestamp=None):
        if timestamp is None :
            timestamp = int(time.time())
        outdata = {"logger":self.number,"data":data,"timestamp":timestamp}
        outstring = json.dumps(outdata)
        urllib.request.urlopen(self.url,data=urllib.parse.urlencode({"entry":outstring}).encode())

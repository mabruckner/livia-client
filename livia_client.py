import urllib.request
import urllib.parse
import json
import time

class logger():
    url=None
    number=None
    def __init__(self,url):
        self.url=url
        response=urllib.request.urlopen(url,data=urllib.parse.urlencode({"authentication":""}).encode())
        number = int(response.read())
        #connect and get id here
        pass

def log(logger,data,timestamp=None):
    if timestamp is None :
        timestamp = int(time.time())
    outdata = {"logger":logger.number,"data":data,"timestamp":timestamp}
    outstring = json.dumps(outdata)
    urllib.request.urlopen(url,data=urllib.parse.urlencode({"entry":outstring}).encode())

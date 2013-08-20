import urllib.request
import json
import time

def log(url,loggerid,data,timestamp=None):
    if timestamp is None :
        timestamp = int(time.time())
    outdata = {"logger":loggerid,"data":data,"timestamp":timestamp}
    outstring = json.dumps(outdata)
    urllib.request.urlopen(url,data=outstring.encode())

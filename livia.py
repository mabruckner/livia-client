import urllib.request
import urllib.parse
import json
import time

class logger():
    def __init__(self,url,project,id=None):
        self.url=url
        self.project = project
        if id is not None :
            self.number = id
        else :
            print("querying ",url+"/projects/"+project+"/addlogger")
            response=urllib.request.urlopen(url+"/projects/"+project+"/addlogger")
            self.number = int(response.read())

    def log(self,data,datatype="",timestamp=None):
        if timestamp is None :
            timestamp = int(time.time())
        outdata = {"logger":self.number,"datatype":datatype,"data":data,"timestamp":timestamp}
        outstring = json.dumps(outdata)
        urllib.request.urlopen(self.url+"/projects/"+self.project,data=urllib.parse.urlencode({"entry":outstring}).encode())

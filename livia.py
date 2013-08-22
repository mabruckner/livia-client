import urllib.request
import urllib.parse
import json
import time

class logger():
    def __init__(self,url,project,id,key):
        self.url=url
        self.project = project
        self.key = key
        self.number = id

    def log(self,data,timestamp=None):
        if timestamp is None :
            timestamp = int(time.time())
        outdata = {"logger":self.number,"data":data,"timestamp":timestamp}
        outstring = json.dumps(outdata)
        urllib.request.urlopen(self.url+"/projects/"+self.project+"/",data=urllib.parse.urlencode({"entry":outstring,"key":self.key}).encode())
    def save(self,fname):
        fp=open(fname,"w")
        json.dump({"id":self.number,"url":self.url,"project":self.project,"key":self.key},fp)
    def load(self,fname):
        fp=open(fname)
        dat=json.load(fp)
        self.number=dat["id"]
        self.url=dat["url"]
        self.project=dat["project"]
        self.key=dat["key"]
    def load(fname):
        fp=open(fname)
        dat=json.load(fp)
        return logger(dat["url"],dat["project"],dat["id"],dat["key"])

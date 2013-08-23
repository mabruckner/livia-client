import urllib.request
import urllib.parse
import json
import time

class logger():
    def __init__(self,url,project,apikey):
        self.url = url
        self.project = project
        self.apikey = apikey

    def log(self,data,timestamp=None):
        if timestamp is None :
            timestamp = int(1000*time.time())
        outdata = {
                    "data":data,
                    "timestamp":timestamp,
                    "apikey":self.apikey
                }

        return_object = {
                    "entry":json.dumps(outdata),
                    "apikey":self.apikey
                }

        if self.url[:-1] == "/":
            url = "{}projects/{}/submit".format(self.url, self.project)
        else:
            url = "{}/projects/{}/submit".format(self.url, self.project)

        print("Response:")
        print(urllib.request.urlopen(url, data=urllib.parse.urlencode(return_object).encode()).read())

    def save(self,fname):
        fp=open(fname,"w")
        json.dump({"url":self.url,"project":self.project,"key":self.apikey},fp)

    def load(self,fname):
        fp=open(fname)
        dat=json.load(fp)
        self.number=dat["id"]
        self.url=dat["url"]
        self.project=dat["project"]
        self.apikey=dat["key"]

    def load(fname):
        fp=open(fname)
        dat=json.load(fp)
        return logger(dat["url"],dat["project"],dat["id"],dat["key"])

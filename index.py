import argparse
import requests
import os

def getPage(url: str):
    if type(url) != str: 
        return "not a url"
    if "web.txt" in os.listdir(): 
        os.remove("web.txt")
    target, web = requests.get(url), open("web.txt", "w")
    web.write(str(target.text))
    web.close()
    return [target.status_code, target.encoding, target.headers["content-type"]]
args = argparse.ArgumentParser(
    prog="pyscraper", 
    description="a python web scraper ", 
)
args.add_argument("-u", "--url")
parser = args.parse_args()
print(getPage(parser.url))
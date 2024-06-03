import argparse
import requests
import os
from bs4 import BeautifulSoup

def getPage(url: str, selectorname: str, className: str): 
    pages = requests.get(url)
    soup = BeautifulSoup(pages.text, 'html.parser')
    return soup.findAll("p", {selectorname: className})
args = argparse.ArgumentParser(
    prog="pyscrape", 
    description="pyscrape is a cli web scraper", 
) 
args.add_argument("-u", "--url")
args.add_argument("-s", "--selectorname")
args.add_argument("-n", "--name")
parse = args.parse_args()
print(getPage(parse.url, parse.selectorname, parse.name))

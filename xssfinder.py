import urllib.request
import sys
import os
import subprocess
import requests
from bs4 import BeautifulSoup as soup
from time import sleep

class XssFinder:

    def __init__(self, target):
        self.target = target
        self.wordlist = open("Wordlists/top1k.txt", 'r').read()
        self.replacedWww = self.target.replace(self.target[:4], '')
        self.replacedHttp = self.target.replace(self.target, 'http://' + self.target)

        self.DiscoverySubd()

    def DiscoverySubd(self):
        subs = subprocess.call('cd /home/espvuln/AutoXss/Sublist3r && python3 sublist3r.py -d '  + self.replacedWww ,shell=True)
        self.connectHost()

    def connectHost(self):
        try:
            urllib.request.urlopen(self.replacedHttp)
            print("Connected")
        except:
            print("Connection has lost")

        self.findAllInputs()

    def findAllInputs(self):
        fields = {}
        req = requests.get(self.replacedHttp).text
        page = soup(req, 'html5lib')
        inputs = page.find_all('input')

        for input in inputs:
            # resim, buton gibi inputları dışlıyoruz
            if input['type'] in ('submit', 'image'):
                continue

            if input['type'] in ('text', 'hidden', 'password', 'textarea', 'search', 'email', 'url'):
                

xss = XssFinder(target=input("Target ( For example: www.google.com ) :  "))



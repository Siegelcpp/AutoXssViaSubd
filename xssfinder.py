import urllib.request
import sys, os, time
import subprocess
import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class XssFinder:

    def __init__(self, target):
        self.target = target
        self.payloads = open("Wordlists/payloads.txt", 'r').read()
        self.replacedWww = self.target.replace(self.target[:4], '')
        self.replacedHttp = self.target.replace(self.target, 'http://' + self.target)
        self.driver = webdriver.Firefox()
        time.sleep(2)
        self.openTarget = self.driver.get(self.replacedHttp)

        self.DiscoverySubd()
    def DiscoverySubd(self):
        #subs = subprocess.call('cd /home/espvuln/AutoXss/Sublist3r && python3 sublist3r.py -d '  + self.replacedWww ,shell=True)
        self.connectHost()

    def connectHost(self):
        try:
            urllib.request.urlopen(self.replacedHttp)
            print("Connected")
        except:
            pass

        self.findAllInputs()

    def findAllInputs(self):
        inputs = self.driver.find_element_by_tag_name("input")

        inputAttrValue = inputs.get_attribute("type")
        print("inputs.get_attribute(\'value\') : {0}".format(inputAttrValue,))


xss = XssFinder(target=input("Target ( For example: www.google.com ) :  "))



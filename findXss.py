from bs4 import BeautifulSoup as soup
from pprint import pprint
from urllib.parse import urljoin
import requests

def extractInputFields(target):
    fields = {}
    req = requests.get(target).text
    page = soup(req, 'html5lib')
    inputs = page.find_all('input')

    for input in inputs:
        # resim, buton gibi inputları dışlıyoruz
        if input['type'] in ('submit', 'image'):
            continue

        if input['type'] in ('text', 'hidden', 'password', 'textarea', 'search', 'email', 'url'):
            print("Maybe is have Xss")


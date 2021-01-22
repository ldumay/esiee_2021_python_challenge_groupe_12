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
import sys
import random
import urllib
import urllib.request
import webbrowser

def stopProgram() :
    print('Il y a une erreur dans votre saisie, veuillez réessayé svp.')
    sys.exit()

def randomNumber(lenght) : #lenght type 'int'
    x = 0
    randomResult = ''
    while x < lenght :
        randomResult += str(random.randint(0, 9))
        x = x+1
    return randomResult #randomResult type 'str'

def checkMonth(month): #month type 'int'
    if month == 1: month = '01'
    elif month == 2: month = '02'
    elif month == 3: month = '03'
    elif month == 4: month = '04'
    elif month == 5: month = '05'
    elif month == 6: month = '06'
    elif month == 7: month = '07'
    elif month == 8: month = '08'
    elif month == 9: month = '09'
    elif month == 10: month = '10'
    elif month == 11: month = '11'
    elif month == 12: month = '12'
    else : month = '00'
    return month #month type 'str'

def generatorKeyDigitMRZ(value): #value type str
    facteurKeys = (7, 3, 1)
    keyGenerated = (value)
    resultat2 = 0
    for (position, car) in enumerate(keyGenerated):
        if car == "<":
            valeur = 0
        elif "0" <= car <= "9":
            valeur = int(car)
        elif "A" <= car <= "Z":
            valeur = ord(car) - 55
        resultat2 += valeur * facteurKeys[position % 3]
    keyGenerated = str(resultat2 % 10)
    return keyGenerated

def openWebPage(url, browser, custom): #value url type str / value browser type int
    # Custom
    if browser == 0 and custom!=None : browser = custom + " %s"
    #Internet Explorer
    elif browser==1 and custom==None : browser = "C:\Program Files\Internet Explorer\iexplore.exe %s"
    # Microsoft Edge
    elif browser == 2 and custom==None : browser = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s"
    #Chrome
    elif browser==3 and custom==None : browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    #--
    webbrowser.get(browser).open_new(url)

def readWebPage(url, debugg): #value url type str

    if debugg==True :
        page = urllib.request.urlopen(url)
        htmlPageUrl = page.url
        htmlPageStatus = page.status
        htmlPage = page.read()
        htmlResponse = [ htmlPageUrl, htmlPageStatus , htmlPage]
        page.close()
        return htmlResponse
    else :
        page = urllib.request.urlopen(url)
        htmlResponse = page.read()
        page.close()
        return htmlResponse

    # -- More
    # htmlResponseType = type(htmlResponse) #type de la requete
    # htmlResponseCode = htmlResponse.code #Code error
    # htmlResponseLenght = htmlResponse.length #poids en byte - ou [ len(htmlResponse) ]
    # htmlResponsePeek = htmlResponse.peek() #--
    # htmlResponseDecode = htmlResponse.decode("UTF-8")

def testSimilarite(chaineRecherchee, chaineTestee):
    chaineRecherchee = str(chaineRecherchee)
    chaineTestee = str(chaineTestee)
    if chaineRecherchee in chaineTestee :
        return True
    else:
        return False
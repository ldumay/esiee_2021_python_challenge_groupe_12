from datas import *
from dependancies import *

def testerPageCore(data):
    goodSource = "rien"
    code = str(data)
    code = code.replace('[', '')
    code = code.replace(']', '')
    # --
    url = "http://univcergy.phpnet.org/scenario3/811193524111958/index.php?open=" + code + "&action=Donne+moi+la+solution"
    #print("url : " + url)
    # --
    htmlPage = readWebPage(url,True)
    resultat = str(htmlPage)
    #--
    htmlUrl = htmlPage[0]
    htmlError = htmlPage[1]
    htmlContent = htmlPage[2]
    #--
    if htmlError==200:
        if not "Votre navigateur ne semble pas supporoter ce fichier" in resultat:
            goodSource = [ htmlUrl, code ]
            #print("- OK - message caché trouvé, pour le code : " + code)
            #print(htmlContent)
        #else:
        #    print("- NO - message caché non trouvé")
        #    #print(htmlContent)
    else:
        print("- page error : "+htmlError)
    return goodSource

def testerPage(url,mode):
    if url=="" and mode==True:
        datas = codeTest()
        #datas = [0]

        # --
        #x = 0
        #datas = []
        #while x < 111111111: # Problème avec => 999999999
        #    datas.append(x)
        #    x = x+1

        # --
        totalTests = len(datas)
        print("nb de tests " + str(totalTests))
        # --
        m = 0
        for data in datas:
            goodSource = testerPageCore(data)
            m = m+1
            print("test "+str(m))
        #--
        if goodSource!="aucune":
            resultat = "\nUrl : "+goodSource[0]+"\nContent : "+goodSource[1]
        else:
            resultat = goodSource
        # --
        print("Resultat : "+resultat+"\nNb tests : "+str(m)+"/"+str(totalTests))
from dependancies import *

def cryptageCesar(chaine, decalage, mode):
    #Variables fixe
    alphabet = desChiffresEtDesLettres(1)
    ponctuation = desChiffresEtDesLettres(5)

    # Mode chiffrage
    if mode==1:
        #suppresion de la ponctuation
        for c in chaine:
            for p in ponctuation:
                if c==p:
                    replace = p
                    chaine.replace(replace,"")

        #Passage en Majuscule
        chainePreparee = chaine.upper()

        #Passage en liste de la chaine
        chainePrepareeList = []
        for cP in chainePreparee:
            chainePrepareeList.append(cP)

        #chiffrage
        chaineChiffre = []
        for cPL in chainePrepareeList:
            if cPL!=" ":
                newPosition = 0
                for position, value in enumerate(alphabet):
                    if cPL==value:
                        newPosition = position+decalage
                        if newPosition > 25:
                            newPosition = newPosition-25-1
                chaineChiffre.append(alphabet[newPosition])
            elif cPL==" ":
                chaineChiffre.append(cPL)

        #Reconstruction de liste en chaine
        chaineResultat = ""
        x = 1
        for cR in chaineChiffre:
            if cR!=" " and x<=5:
                chaineResultat += cR
                x = x + 1
            elif cR!=" " and x>5:
                x = 2
                chaineResultat += " "+cR

        #--
        return chaineResultat

    # Mode déchiffrage
    elif mode == 2:
        #Suppresion des espaces
        chainePreparation = []
        for c in chaine:
            if c!=" ":
                chainePreparation.append(c)
        #print(chainePreparation)

        #Déchiffrage
        chaineDeChiffre = []
        for cP in chainePreparation:
            newPosition = 0
            for position, value in enumerate(alphabet):
                if cP==value:
                    newPosition = position-decalage
                    if newPosition > 25:
                        newPosition = newPosition-25-1
            chaineDeChiffre.append(alphabet[newPosition])

        # Reconstruction de liste en chaine
        chaineResultat = ""
        for cDC in chaineDeChiffre:
            chaineResultat += cDC

        # --
        return chaineResultat

    # Erreur
    else:
        return "Merci de choisir une chaine et un mode."
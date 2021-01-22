from datetime import date
from dependancies import *

def generateCNI():
    debugg = False  # True OU False

    print('Quelques infos avant svp :')

    # --Nom
    nom = input('- nom (25 chars max) : ')
    nomCNI = nom.upper()
    nomCNILenght = len(nomCNI)
    while nomCNILenght < 25:
        nomCNI += '<'
        nomCNILenght += 1
    # --Prenom
    prenom = input('- prenom (14 chars max) : ')
    prenomCNI = prenom.upper()
    prenomCNILenght = len(prenomCNI)
    while prenomCNILenght < 14:
        prenomCNI += '<'
        prenomCNILenght += 1
    # --DateNaissance
    dateNaissance = input('- dateNaissance - JJ/MM/AAAA : ')
    if len(dateNaissance) < 8: stopProgram()
    dateNaissanceTemp = dateNaissance.split('/')
    x = 2
    dateNaissance = ''
    for naiss in dateNaissanceTemp:
        dateNaissance += dateNaissanceTemp[x]
        x = x - 1
    # --Departement
    departementTemp = []
    departement = input('- departement - 95000 : ')  # 95 ou 95500
    if len(departement) < 2: stopProgram()
    x = 0
    for dep in departement:
        departementTemp.append(departement[x])
        x = x + 1
    departement = departementTemp[0] + departementTemp[1]
    # --Sexe
    sexe = input('- sexe - homme OU femme : ')
    if sexe == 'femme':
        sexe = 'F'
    else:
        sexe = 'M'
    if sexe == 'femme':
        genre = 'Mme'
    else:
        genre = 'Mr'

    # --Dates
    today = date.today()
    x = 0
    anneeTemp = []
    anneeActuel = str(today.year)
    for annee in anneeActuel:
        anneeTemp.append(anneeActuel[x])
        x = x + 1
    anneeActuel = anneeTemp[2] + anneeTemp[3]
    moisActuel = str(checkMonth(today.month))

    # --PréparationsDesInformationsDeLaCNI
    typeTitre = 'ID'
    pays = 'FRA'
    numDossierTitre = randomNumber(4)
    numTitre = anneeActuel + moisActuel + departement + numDossierTitre
    keyTitre = generatorKeyDigitMRZ(numTitre)  # Clé de controle des caractères 1-12 précédents
    siteEmetteur = randomNumber(4)  # Identifiant de l'agent ayant enregistré la carte
    keyDateNAiss = generatorKeyDigitMRZ(str(dateNaissance))  # Clé de controle de la date de naissance
    # --
    resultKeyCode_Part_Top = typeTitre + pays + nomCNI + departement + siteEmetteur
    resultKeyCode_Part_Bottom_Tmp = numTitre + keyTitre + prenomCNI + dateNaissance + keyDateNAiss + sexe
    # --
    keyCNI = generatorKeyDigitMRZ(resultKeyCode_Part_Top + resultKeyCode_Part_Bottom_Tmp)  # Clé de contrôle de la CNI
    # --
    resultKeyCode_Part_Bottom = resultKeyCode_Part_Bottom_Tmp + keyCNI

    # --CheckKeys
    if (debugg == True): print(
        '\nKeys => keyTitre : ' + keyTitre + ' - keyDateNAiss : ' + keyDateNAiss + ' - keyCNI : ' + keyCNI)
    if (debugg == True): print(
        '\nchecking : ' + typeTitre + ' ' + pays + ' ' + nomCNI + ' ' + departement + ' ' + siteEmetteur)
    if (debugg == True): print(
        'checking : ' + numTitre + ' ' + keyTitre + ' ' + prenomCNI + dateNaissance + ' ' + keyDateNAiss + ' ' + sexe + ' ' + keyCNI)

    resultKeyCode_Part_Top_Lenght_Prevue = 36
    resultKeyCode_Part_Bottom_Lenght_Prevue = 36
    resultKeyCode_Part_Top_Lenght_Reelle = len(resultKeyCode_Part_Top)
    resultKeyCode_Part_Bottom_Lenght_Reelle = len(resultKeyCode_Part_Bottom)

    print('\nVoici votre clé de CNI ' + genre + ' ' + prenom + ' ' + nom.upper() + '\n')
    print(resultKeyCode_Part_Top + '\n' + resultKeyCode_Part_Bottom)
    # --ForDebugg
    if (debugg == True): print(
        'KeyTop - longueur prévue : ' + str(resultKeyCode_Part_Top_Lenght_Prevue) + ' - lenght reélle : ' + str(
            resultKeyCode_Part_Top_Lenght_Reelle))
    if (debugg == True): print(
        'KeyBottom  - longueur prévue : ' + str(resultKeyCode_Part_Bottom_Lenght_Prevue) + ' - lenght reélle : ' + str(
            resultKeyCode_Part_Bottom_Lenght_Reelle))
# Git Version : 0.0.3

# imports :
from datetime import date
from dependancies import *

# start code
if __name__ == '__main__':

    print('Quelques infos avant svp :')

    #--Nom
    nom = input('- nom : ')
    nomCNI = nom.upper()
    nomCNILenght = len(nomCNI)
    while nomCNILenght < 25:
        nomCNI += '<'
        nomCNILenght += 1
    #--Prenom
    prenom = input('- prenom : ')
    prenomCNI = prenom.upper()
    prenomCNILenght = len(prenomCNI)
    while prenomCNILenght < 14:
        prenomCNI += '<'
        prenomCNILenght += 1
    #--DateNaissance
    dateNaissance = input('- dateNaissance - JJ/MM/AAAA : ')
    if len(dateNaissance) < 8: stopProgram()
    dateNaissance = dateNaissance.replace('/','')
    #--Departement
    departementTemp = []
    departement = input('- departement - 95000 : ') #95 ou 95500
    if len(departement) < 2 : stopProgram()
    x = 0
    for dep in departement :
        departementTemp.append(departement[x])
        x = x+1
    departement = departementTemp[0] + departementTemp[1]
    #--Sexe
    sexe = input('- sexe - homme OU femme : ')
    if sexe == "femme":
        sexe = 'F'
    else :
        sexe = 'M'
    if sexe == "femme":
        genre = 'Mme'
    else :
        genre = 'Mr'

    #--Dates
    today = date.today()
    x = 0
    anneeTemp = []
    anneeActuel = str(today.year)
    for annee in anneeActuel :
        anneeTemp.append(anneeActuel[x])
        x = x+1
    anneeActuel = anneeTemp[2] + anneeTemp[3]
    moisActuel = str(checkMonth(today.month))

    #--Autres
    typeTitre = 'ID'
    pays = 'FRA'
    numDossierTitre = randomNumber(4)
    numTitre = anneeActuel + moisActuel + departement + numDossierTitre
    keyTitre = '-' #Clé de controle des caractères 1-12 précédents
    siteEmetteur = randomNumber(4) #Identifiant de l'agent ayant enregistré la carte
    keyDateNAiss = '-' #Clé de controle de la date de naissance
    keyCNI = '-' #Clé de contrôle de la CNI

    flechtop = '<<<<<'
    flechbottom = '<<<<<'

    resultKeyCode_Part_1_Lenght = 36
    resultKeyCode_Part_2_Lenght = 36

    resultKeyCode_Part_1 = typeTitre + pays + nomCNI + departement + siteEmetteur
    resultKeyCode_Part_2 = numTitre + keyTitre + prenomCNI + dateNaissance + keyDateNAiss + sexe + keyCNI

    print('\nVoici votre clé de CNI '+genre+' '+prenom+' '+nom.upper()+'\n')
    print(resultKeyCode_Part_1 + '\n' + resultKeyCode_Part_2)
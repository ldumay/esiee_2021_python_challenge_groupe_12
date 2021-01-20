import sys
import random

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
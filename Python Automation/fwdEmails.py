# Last updated 8/27/2021
def fwdEmail():

    usa_hp = ['ingrid.alvarado@hp.com', 'angelica.arriaga1@hp.com',
    'suriel.deleon@hp.com', 'michael.mack@hp.com', 'george.doukas@hp.com']

    méj_hp = ['victor.manuel.leon.diaz@hp.com', 'michael.mack@hp.com']


    while True:
        
        print("Where are you sending the MACD to?")
        send_to = int(input("Press 1 for USA, or 2 for Méjico"))
        if send_to == 1:
            return usa_hp
        elif send_to == 2:
            return méj_hp
        else:
            print("ERROR! You must enter 1 or 2")

    for i in usa_hp:
        print(i, ';')

def typeSignature():
    print('Zachary B. Ellis')

#typeSignature()
fwdEmail()


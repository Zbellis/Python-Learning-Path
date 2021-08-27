# Last updated 8/27/2021
def fwdMACD():
    send_to = int(input("Representatives from HP 1 for USA, or 2 for Mejico: "))

    if send_to == 1:
        return fwdEmailUSA()
    elif send_to == 2:
        return fwdEmailMejico()

def fwdEmailUSA():
    us_hp = ['ingrid.alvarado@hp.com', 'angelica.arriaga1@hp.com',
    'suriel.deleon@hp.com', 'michael.mack@hp.com', 'george.doukas@hp.com']

    for i in us_hp:
        print(i, ';')

def fwdEmailMejico():
    mej_hp = ['victor.manuel.leon.diaz@hp.com', 'michael.mack@hp.com']

    for i in mej_hp:
        print(i, ';')

fwdMACD()

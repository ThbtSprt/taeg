from dateutil.relativedelta import relativedelta
from decimal import Decimal as d
import frdate


def formule_test(nb_mens, liste_mens, TAEG, montant_credit, frais=0, decalage=1/12):
    '''
    *nb_mens :
        nombre de mensualités
    *liste_mens :
        liste des mensualités : automatisable depuis la fonction liste_M()
    *TAEG :
        TAEG (en %)
    *montant_credit :
        montant total emprunté
    *frais :
        frais non-inclus dans le montant des mensualités
    *decalage :
        nombre de jours entre le déblocage des fonds et la 1ere mensualités'''

    somme = 0
    for i in range(len(liste_mens)):
        numerateur = d(liste_mens[i])
        exposant = (d(i)/12)+d(decalage)
        denominateur = pow((1+d(TAEG)/100), exposant)
        somme += numerateur/denominateur
    resultat = somme+d(frais)-d(montant_credit)
    return resultat


def liste_M(nb_mens, montant_mens, num_mens_spec='', montant_mens_spec=''):
    '''
    *nb_mens :
        nombre de mensualités
    *montant_mens :
        montant des mensualités principales (hors assurance)
    *num_mens_spec (facultatif) :
        numéro(s) d'ordre des éventuelles mensualités spéciales
        (à séparer par une double virgule : ex : '23,,24')
    *montant_mens_spec (facultatif) :
        montant des mensualités spéciales, dans le même ordre que num_mens_spec
        (à séparer par une double virgule : ex : '32.33,,32.33,,32.333')'''

    liste = []
    for i in range(int(nb_mens)):
        liste.append(montant_mens)
    if num_mens_spec != '':
        num_mens_spec = num_mens_spec.split(',')
        montant_mens_spec = montant_mens_spec.split(',')
        for i in range(len(num_mens_spec)):
            liste[int(num_mens_spec[i])-1] = montant_mens_spec[i]
    return liste


def decalage(remise, premiere_mens):
    if remise != '':
        debloc = frdate.conv(remise, True)
        premiere = frdate.conv(premiere_mens, True)
        deca = relativedelta(premiere, debloc)
        annee = ((debloc+relativedelta(days=deca.days))-(debloc+relativedelta(days=deca.days)-relativedelta(years=1))).days
        D = deca.years+d(deca.months)/12+d(deca.days)/annee
    else:
        D = d(1/12)
    return D


def calcul(montant_credit, nb_mens, montant_mens, frais='', num_mens_spec='', montant_mens_spec='', deblocage='', premiere_mens=''):
    '''
    ARGUMENTS :

    *montant_credit :
        montant total emprunté
    *nb_mens :
        nombre de mensualités
    *montant_mens :
        montant des mensualités principales (hors assurance)
    *frais :
        montant des frais non-compris dans les mensualités
    *num_mens_spec (facultatif) :
        numéro(s) d'ordre des éventuelles mensualités spéciales
        (à séparer par une virgule : ex : '23,24')
    *montant_mens_spec (facultatif) :
        montant des mensualités spéciales, dans le même ordre que num_mens_spec
        (à séparer par une virgule : ex : '32.33,32.33,32.333')
    *deblocage (facultatif):
        date de déblocage des fonds
    *premiere_mens (facultatif) :
        date du premier prélèvement d'échéance
    '''

    mensualites = liste_M(nb_mens, montant_mens, num_mens_spec, montant_mens_spec)
    if frais == '':
        frais = 0
    taux = d('1')    # On commence à tester la formule_test avec un taux de 1%
    k = d('100')       # On commence à tâtonner en ajoutant ou soustrayant 100 %
    if deblocage != '' and premiere_mens != '':
        report = decalage(deblocage, premiere_mens)
    else:
        report = 1/12
    test = formule_test(nb_mens, mensualites, taux, montant_credit, frais, report)
    while abs(test) > 0.00001:
        for i in range(10):
            if test > 0:
                taux += k
            else:
                taux -= k
            test = formule_test(nb_mens, mensualites, taux, montant_credit, frais, report)
            #print(test)
        k = k/10
    return float(taux)

# la liste est la structures de donnee optimale
def moneyBack(amount, coins):
    i = 0
    n = len(coins)
    chosen = [0] * n
    for i in range(n - 1, -1, -1):
        while amount >= coins[i]:
            amount -= coins[i]
            chosen[i] += 1
    assert amount == 0
    return chosen


amount = 16000
coins = [250, 500, 1000, 5000, 10000, 20000, 50000, 100000]
print(moneyBack(amount, coins))
# iterative
def rendreMonaieIt(amount, coins):
    i = 0
    n = len(coins)
    chosen = [0] * n
    for i in range(n - 1, -1, -1):
        while amount >= coins[i]:
            amount -= coins[i]
            chosen[i] += 1
    assert amount == 0
    return chosen


amount2 = 5000
coins = [500, 1000]
print(rendreMonaieIt(amount2, coins))


# recursive
def rendreMonaieRec(ammount):
    cinqMille = 5000
    mille = 1000
    nombreBillet = []
    i = 0
    cinq = int(ammount / cinqMille)
    ammount = ammount % cinqMille
    un = int(ammount / mille)
    ammount = ammount % mille
    nombreBillet.insert(i, cinq)
    nombreBillet.insert(i + 1, un)
    return nombreBillet
print(rendreMonaieRec(7000))
# liste comprehension


# recursive
def toutRendreMonnaiRec(monaie):
    cinqMille = 5000
    mille = 1000
    val=[]
    cinq = int(monaie / cinqMille)
    un = int(monaie / mille)
    monaieUn = cinq
    mon = monaie % cinqMille
    monaieDeux =mon/mille
    monaieTrois=un
    monaieQuatre=monaie%un
    val.insert(1,monaieUn)
    val.insert(2,monaieDeux)
    val.insert(3,monaieTrois)
    val.insert(4,monaieQuatre)
    return val
print(toutRendreMonnaiRec(7000))
#iteratif
def touRendreIteratif(monaie):
    cinqMille = 5000
    mille = 1000
    i=0
    j=0
    v=[]

    while i<monaie or j<monaie:
       i=i+1000
       j=j+5000
       monaieTemp=monaie
       monaieTemp2=monaie
       one=int(monaieTemp/cinqMille)
       onetemp=monaie%cinqMille
       two=onetemp/mille

       three = int(monaieTemp2 / mille)
       threeTem=three%mille
       four=int(threeTem/cinqMille)
    v.insert(0,one)
    v.insert(1,two)
    v.insert(2,three)
    v.insert(3,four)
    return v
print(touRendreIteratif(7000))
# liste comprehension

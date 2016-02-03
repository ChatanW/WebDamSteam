#-*- coding:Utf-8 -*-
#SURTOUT NE PAS OUBLIER CETTE PUTAIN DE LIGNE DE MERDE CI DESSUS
#APPAREMENT CA REGLE TOUS LES PROBLEMES D'ENCODAGE !!!
import score2
import steamapi

steamapi.core.APIConnection(api_key="5BB69AE39C3B27011CE4CCDA8606F427")

seya = steamapi.user.SteamUser(76561198060771978)
seya_meetic = score2.SteamMeeticUser(seya)

fl = seya_meetic.friendlist() 

res = []
for friend in fl: 
    res += [(str(friend),seya_meetic.score(friend)[1])]
res.sort(key = lambda x: x[1])

for (name, score) in reversed(res): 
    print(name+" : "+str(score))
'''
def lol(x):
    for i in range(0,42): 
        strr = str(i+1)+" "+" "+str(x.pop())
        print(strr)#.encode(errors='strict'))

print("lél")
lol(fl)
'''
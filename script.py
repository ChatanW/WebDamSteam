#-*- coding:Utf-8 -*-
#SURTOUT NE PAS OUBLIER CETTE PUTAIN DE LIGNE DE MERDE CI DESSUS
#APPAREMENT CA REGLE TOUS LES PROBLEMES D'ENCODAGE !!!
import score2
import steamapi
import sys

steamapi.core.APIConnection(api_key="5BB69AE39C3B27011CE4CCDA8606F427")


def script(id_user):
    user = steamapi.user.SteamUser(id_user);
    user_meetic = score2.SteamMeeticUser(user)
    user_teamates = user_meetic.best_scores_file("scriptPython/list_gens_id_1.txt",100,nb_best=7)
    return (user_teamates)

try:
    result = script(int(sys.argv[1]))
    for (teamate, score, games) in result:
        print (teamate.id)
        print (score)
        for game in games:
            print (game[0])
            print (game[1])
            print (game[3])
        print ("##CHANGEMENT123321##")
except:
    print "Problème dans le script"

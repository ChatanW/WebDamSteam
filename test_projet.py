#-*- coding:Utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import score1
import steamapi

steamapi.core.APIConnection(api_key="75F43EA5FA862713704515E6904DA5FD")

'''
me = steamapi.user.SteamUser(userurl="chatanw")
me_meetic = score1.SteamMeeticUser(me)
print(me_meetic.best_scores_file("list_gens_id_2.txt",nb_best=3))
'''

def plusieurs_tests(id_user, name_file_id, list_filtr, list_pond, list_pond_recent, nb_best):
    test_user = steamapi.user.SteamUser(id_user)
    user_meetic = score1.SteamMeeticUser(test_user)
    print(("On travaille avec l'user nomme" + test_user.name).encode('utf8'))
    print('\n')
    for filtr in list_filtr:
        for pond in list_pond:
            for pond_recent in list_pond_recent:
                user_teammates = user_meetic.best_scores_file(name_file_id, filtr, pond, pond_recent, nb_best)
                print("Le ratio_filtr vaut : " + str(filtr))
                print("Le coef_pond vaut : " + str(pond))
                print("Le coef_pond_recent vaut : " + str(pond_recent))
                print('\n')
                for (user, score, games) in user_teammates:
                    if user == test_user:
                        ()
                    else:
                        print(user)
                        print(score)
                        for game in games:
                            phrase = game[0] + " temps : " + str(game[1])
                            phrase = phrase.encode('utf8')
                            print(phrase)
                        print('\n')
                print('\n')

plusieurs_tests(76561198060771978, "list_gens_id_2.txt", [1], [1], [0, 0.5, 1], 3)

'''
seya = steamapi.user.SteamUser(76561198060771978)
seya_meetic = score1.SteamMeeticUser(seya)
seya_teammates = seya_meetic.best_scores_file("list_gens_id_2.txt",nb_best=6)
for (user, score, games) in seya_teammates:
    if user == seya:
        ()
    else:
        print(user)
        print(score)
        for game in games:
            print(game[0] + " temps : " + str(game[1]))
        print('\n')
'''

'''
poli = steamapi.user.SteamUser(76561198074242096)
poli_meetic = score1.SteamMeeticUser(poli)
poli_teammates = poli_meetic.best_scores_file("list_gens_id_2.txt",nb_best=15)
for (user, score, games) in poli_teammates:
    if user==poli:
       ()
    else:
        print(user)
        print(score)
        for game in games:
            print(game[0] + " temps : " + str(game[1]))
        print('\n')
'''

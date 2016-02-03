#-*- coding:Utf-8 -*-
import score2
import steamapi

steamapi.core.APIConnection(api_key="5BB69AE39C3B27011CE4CCDA8606F427")

'''
me = steamapi.user.SteamUser(userurl="chatanw")
me_meetic = score1.SteamMeeticUser(me)
print(me_meetic.best_scores_file("list_gens_id_2.txt",nb_best=3))
'''


seya = steamapi.user.SteamUser(76561198060771978)
seya_meetic = score2.SteamMeeticUser(seya)


seya_teammates = seya_meetic.best_scores_file("list_gens_id_3.txt",100,nb_best=7)
for (user, score, games) in seya_teammates:
    print(user)
    print(score)
    for game in games:
        print(game[0] + " temps : " + str(game[1]))
    print('\n')


'''
for game in seya.games: 
    print(game._id)
'''

'''
print(seya.games) 
print('\n')
seya.games.sort(key = lambda game: game._id)
print(seya.games)
print(seya.games.pop(0))
print(seya.games) 
'''

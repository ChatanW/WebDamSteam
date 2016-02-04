#-*- coding:Utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import steamapi


steamapi.core.APIConnection(api_key="75F43EA5FA862713704515E6904DA5FD")
me = steamapi.user.SteamUser(userurl="chatanw")
#print(me.privacy)
#print(me.level)
#print(me.friends)
#print(me.games)
#print(me.badges)

'''
polimegalo = steamapi.user.SteamUser(76561198074242096)
poli_badges = polimegalo._badges
print(poli_badges)
print(poli_badges.badges)
for badge in poli_badges:
    print(badge.completion_time)
#print(polimegalo.badges)
poli_group = polimegalo.group
print(poli_group.guid)
'''
grosxor = steamapi.user.SteamUser(76561198076634820)
'''
grosxor_badges = grosxor._badges.badges
print(grosxor_badges)
for badge in grosxor_badges:
    print(badge.completion_time)
#print(grosxor.badges)
'''

'''
my_friends = me.friends + [me]
for friend in my_friends :
    friend_badges = friend._badges.badges
    for badge in friend_badges:
        print(badge)
        truc_ecrire = (friend.name + " a complété le badge d'id  " + str(badge.badgeid) + " il y a " + str(badge.completion_time) + " secondes.")
        truc_ecrire = truc_ecrire.encode('utf8')
        print(truc_ecrire)
'''


games_grosxor = grosxor.games
'''
games_grosxor_name = []
compte = 1
for game in games_grosxor:
    games_grosxor_name.append(game.name.encode('utf8'))
games_grosxor_name.sort(key=str.lower)
for game in games_grosxor_name:
    print(game) 
    #print(compte)
    compte += 1
'''
    

games_chatan = me.games
print("Grosxor a " + str(len(games_grosxor)) + " jeux, alors que j'en ai " +  str(len(games_chatan)))
commun_games = []
for game in games_grosxor:
    if game in games_chatan:
        commun_games.append(game)
print("On en a " + str(len(commun_games)) + " en commun")
for game in commun_games:
    print(game.name)


'''
my_friends = me.friends + [me]
for friend in my_friends :
    print(friend.name + " a " + str(len(friend.games)) + " jeux")
'''

'''
my_friends = me.friends + [me]
for friend in my_friends :
    for game in friend.games:
        truc_ecrire = (friend.name + " a joue " + str(game.playtime_forever) + " minutes au jeu " + game.name)
        truc_ecrire = truc_ecrire.encode('utf8')
        print(truc_ecrire)
'''

'''
my_friends = me.friends + [me]
for friend in my_friends:
    my_friends.remove(friend)
    games = friend.games
    for be_friend in my_friends:
        games2 = be_friend.games
        
        for game in games:
            for game2 in games2:
                if game.name == game2.name and game2.playtime_forever > 0:
                    time_ratio = (game.playtime_forever - game2.playtime_forever)  / game2.playtime_forever
                    if time_ratio >= -0.1 and time_ratio <= 0.1:
                        phrase = friend.name + " (" + str(game.playtime_forever) + ")" + " et " + be_friend.name + " (" + str(game2.playtime_forever) + ")" + " sont faits pour jouer ensemble a " + game.name + ", le ratio vaut " + str(time_ratio)
                        phrase = phrase.encode('utf8')
                        print(phrase)
'''

'''
À partir de ce travail, il faut mettre des fonctions de "quel est mon meilleur teammate ?"
En gros, quand quelqu'un s'incrit, on calcule le score de rapprochement entre lui est chaque membre déjà inscrit 
(cf. bdd en cours de création) et on prend les meilleurs. Ce score est calculé, en première approximation, en comptant 
le nombre de jeux sur lesquels ils ont joué quasiment autant de temps (non nul !). On pourra pondéré cela avec le temps 
de jeu (etre comptatible sur 25 minutes n'est pas hyper pertinent) puis, à voir (je suis pas encore bien convaincu et 
surtout ça pose des pb, donc dans un premier temps il faudra conserver la filtration et juste pondérer par le temps de jeu) 
avec l'inverse du "ratio" (et donc enlever la filtration par ratio). On pourra aussi filtrer par heures auquels les gens jouent, 
mais c'est plus compliqué/restreint (paramètre privé et donc pas toujours visible). On pourra aussi s'interesser au temps 
de jeux récents (pertinent !!!)
'''

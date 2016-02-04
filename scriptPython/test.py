#-*- coding:Utf-8 -*-
import steamapi
steamapi.core.APIConnection(api_key="75F43EA5FA862713704515E6904DA5FD")
me = steamapi.user.SteamUser(userurl="chatanw")
#print(me.level)
#print(me.friends)
list_players = [me]
current_list = [me]
'''
my_friends = me.friends
for player in my_friends:
    print(player.name)
    print(player.level)
    try:
        print(player.friends)
    except: 
        print("Il veut pas qu'on voit ses amis :(")
'''
#print("Coucou")
i = 0
nb_boucles = 1
#no_friends_nb = 0
no_friends_list = []
while i < nb_boucles:
    i = i + 1
    current_friends = []
    for player in current_list:
        try:
            friends = player.friends
        except:
            friends = []
            #no_friends_nb = no_friends_nb + 1
            no_friends_list.append(player)
        for friend in friends:
            if (friend not in list_players):
                current_friends.append(friend)
                list_players.append(friend)
    current_list = current_friends

'''
#Ici, on a la liste brut
print("La liste des gens que j'ai pu obtenir en " + str(nb_boucles) + " tours de boucles :)")
print(list_players)
print(len(list_players))
print("La liste des gens dont j'ai pa pu voir les amis :(")
print(no_friends_list)
print(len(no_friends_list))
'''
#Ici, on liste simplement les id des gens 
for player in list_players:
    print(player.id)


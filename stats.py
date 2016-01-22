#coding: utf-8
from __future__ import unicode_literals
from __future__ import division
import score1
import steamapi

steamapi.core.APIConnection(api_key="75F43EA5FA862713704515E6904DA5FD")

def nombre_amis_moyens(name_file_id):
    nb_friends = 0
    nb_public_users = 0
    nb_private_users = 0
    file_id = open(name_file_id, "r")
    for ligne in file_id:
         user = steamapi.user.SteamUser(int(ligne))
         try:
             nb_friends += len(user.friends)
             nb_public_users += 1
         except:
             nb_private_users += 1
    average = nb_friends / nb_public_users
    print(nb_friends)
    print(nb_public_users)
    print(average)
    print(nb_private_users)

#def joue est la limite de temps de jeu pour définir qu'on y a joué, c'est pas pareil de l'avoir ouvert 5 minutes que d'y avoir joué au moins 3 heures !

def ratio_jeux_joues(user, def_joue):
    nb_jeux_owned = 0
    nb_jeux_played = 0
    try:
        games = user.games
        for game in games:
            nb_jeux_owned += 1
            if game.playtime_forever > def_joue:
                nb_jeux_played += 1
        return nb_jeux_played/nb_jeux_owned
    except:
        return -1

def ratio_jeux_joues_moyenne(name_file_id, def_joue):
    nb_users = 0
    ratio_total = 0
    file_id = open(name_file_id, "r")
    for ligne in file_id:
         user = steamapi.user.SteamUser(int(ligne))
         ratio = ratio_jeux_joues(user, def_joue)
         if ratio > -1:
             nb_users += 1
             ratio_total += ratio
    ratio_moyen = ratio_total / nb_users
    print(ratio_moyen)




#nombre_amis_moyens("list_gens_id_3.txt")
ratio_jeux_joues_moyenne("list_gens_id_3.txt",0)
ratio_jeux_joues_moyenne("list_gens_id_3.txt",59)
ratio_jeux_joues_moyenne("list_gens_id_3.txt",179)

#coding: utf-8
from __future__ import unicode_literals
from __future__ import division
import steamapi


steamapi.core.APIConnection(api_key="75F43EA5FA862713704515E6904DA5FD")
me = steamapi.user.SteamUser(userurl="chatanw")
seya = steamapi.user.SteamUser(76561198060771978)

my_games = me.games
seya_games = seya.games


for game in seya_games:
    print(game.name)
    print(game.playtime_forever)
    try:
        print(game.playtime_2weeks)
    except:
        print("problem playtime_2weeks")
    try:
        print(game.appid)
    except:
        print("problem appid")
    try:
        print(game.has_community_visible_stats)
    except:
        print("problem community ...")
    print('\n')

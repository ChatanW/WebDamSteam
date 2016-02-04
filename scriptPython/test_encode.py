#-*- coding:Utf-8 -*-
import score2
import steamapi

steamapi.core.APIConnection(api_key="5BB69AE39C3B27011CE4CCDA8606F427")

seya = steamapi.user.SteamUser(76561198060771978)
seya_meetic = score2.SteamMeeticUser(seya)

games = seya.games

for game in games: 
    print(game)


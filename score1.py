#coding: utf-8
from __future__ import unicode_literals
from __future__ import division
import steamapi

__author__ = 'Chatan'


class SteamMeeticUser:
    def __init__(self, steamuser):
        """
        We create a new steam user of our corresponding app using its SteamUser class

        :param steamuser: The user's rofile from the api
        :type steamuser: steamapi.user.SteamUser
        """
        self._steamuser = steamuser

    @property
    def steamuser(self):
        return self._steamuser

    '''
    games_corresponding va renvoyé la liste des jeux que j'ai en "commun" avec un autre user
    '''
    def games_corresponding(self, user_to_match, ratio_filtr=0.1):
        my_games = self.steamuser.games
        try:
            its_games = user_to_match.games
        except:
            its_games = []
        result_games = []
        for game in my_games:
            for game2 in its_games:
                if game.name == game2.name and game.playtime_forever > 0:
                    time_ratio = (game.playtime_forever - game2.playtime_forever)  / game.playtime_forever
                    if time_ratio >= -ratio_filtr and time_ratio <= ratio_filtr:
                        try:
                            time_recent = game2.playtime_2weeks
                        except:
                            time_recent = 0
                        result_games += [(game.name, game2.playtime_forever, time_recent, time_ratio)]
        return result_games

    '''
    score1 va calculer le score de pertinence entre nous est un autre user_steam, à partir de nos temps de jeux respectifs.
    user_to_match est l'user steam avec lequel on calcule le score, c'est un SteamUser
    ratio_filtr est l'écart relatif que l'on permet sur la filtration des jeux
    pond_time est le coef que l'on attribue au temps de jeux (correspondre sur 2500 min de jeux est beaucoup plus pertinent que sur 25 min).
    '''
    def score1(self, user_to_match, ratio_filtr=0.1, pond_time=1, pond_time_recent=0.5):
        good_games = self.games_corresponding(user_to_match, ratio_filtr)
        score = 0
        for (game, time, time_recent, ratio) in good_games:
            score += pond_time * time + pond_time_recent * time_recent
        return (score, good_games)
        
    '''
    best_scores envoie la liste des users me correspondant le mieux, à partir d'une liste d'users
    '''
    def best_scores(self, list_users, ratio_filtr=0.1, pond_time=1, pond_time_recent=0.5, nb_best=5):
        nb_results = 0
        list_results = []
        for user in list_users:
            (score, games) = self.score1(user, ratio_filtr, pond_time, pond_time_recent)
            ind = nb_results - 1
            while ind >-1 and score > list_results[ind][1]:
                ind = ind - 1
            if ind == nb_results - 1:
                if nb_results<nb_best:
                    list_results.append((user, score, games))
                    nb_results += 1
            else:
                if nb_results<nb_best:
                    list_results = list_results[0:ind+1] + [(user, score, games)] + list_results[ind+1:nb_results]
                    nb_results += 1
                else:
                    list_results = list_results[0:ind+1] + [(user, score, games)] + list_results[ind+1:nb_results - 1]
        return list_results



    '''
    best_scores_file envoie la liste des users me correspondant le mieux, à partir d'une liste d'users issue d'un fichier d'id
    '''
    def best_scores_file(self, name_file_id, ratio_filtr=0.1, pond_time=1, pond_time_recent=0.5, nb_best=5):
        nb_results = 0
        list_results = []
        file_id = open(name_file_id, "r")
        for ligne in file_id:
            user = steamapi.user.SteamUser(int(ligne))
            (score, games) = self.score1(user, ratio_filtr, pond_time, pond_time_recent)
            ind = nb_results - 1
            while ind >-1 and score > list_results[ind][1]:
                ind = ind - 1
            if ind == nb_results - 1:
                if nb_results<nb_best:
                    list_results.append((user, score, games))
                    nb_results += 1
            else:
                if nb_results<nb_best:
                    list_results = list_results[0:ind+1] + [(user, score, games)] + list_results[ind+1:nb_results]
                    nb_results += 1
                else:
                    list_results = list_results[0:ind+1] + [(user, score, games)] + list_results[ind+1:nb_results - 1]
        return list_results      
            

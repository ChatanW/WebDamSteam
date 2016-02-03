#-*- coding:Utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import steamapi

__author__ = 'Seyaryuki'


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

    def palier(self, game): 
        result_palier = []
        time = game.playtime_forever 
        if time == 0: 
            result_palier += [0]
        if 0 < time <= (15*60): 
            result_palier += [1]
        if (8*60) <= time <= (60*60):
            result_palier += [2]
        if (40*60) <= time <= (120*60):
            result_palier += [3]
        if (90*60) <= time <= (550*60):
            result_palier += [4]
        if (500*60) <= time <= (1200*60):
            result_palier += [5]
        if (800*60) <= time:
            result_palier += [6]
        return result_palier
    '''
    games_corresponding va renvoyé la liste des jeux que j'ai en "commun" avec un autre user
    '''
    def games_corresponding(self, user_to_match):
        my_games = self.steamuser.games
        my_games.sort(key = lambda game: game._id)
        try:
            its_games = user_to_match.games
        except:
            its_games = []
        its_games.sort(key = lambda game: game._id)
        result_played_games = []
        result_not_played_games = [] 
        my_i = 0
        its_i = 0
        while my_i < len(my_games) and its_i < len(its_games): 
            my_game = my_games[my_i]
            its_game = its_games[its_i]
            if my_game._id == its_game._id: 
                if my_game.playtime_forever > 0 and its_game.playtime_forever > 0: 
                    result_played_games += [(my_game.name, my_game.playtime_forever, self.palier(my_game), its_game.playtime_forever, self.palier(its_game))]
                else: 
                    result_not_played_games += [(my_game.name, my_game.playtime_forever, self.palier(my_game), its_game.playtime_forever, self.palier(its_game))]
                my_i += 1
                its_i += 1
                continue 
            if my_game._id < its_game._id: 
                my_i += 1
            else: 
                its_i += 1
        return (result_played_games, result_not_played_games) 

    ''' 
    palier_dist calcule la distance minimale entre les paliers d'un jeu, et renvoie un multiplicateur de score
    ''' 
    def palier_dist(self, l1, l2):
        d = 7
        for p1 in l1:
            for p2 in l2: 
                if d > abs(p1-p2): 
                    d = abs(p1-p2)
        if d == 0: 
            return 1.00
        if d == 1: 
            return 0.80 
        if d == 2: 
            return 0.55
        if d == 3: 
            return 0.10 
        if d == 4: 
            return 0.01 
        if d == 5: 
            return 0.00
        if d == 6: 
            return 0.00 
        
    '''
    score2 va calculer le score de pertinence entre nous est un autre user_steam, 
    à partir de nos temps de jeux respectifs.
    user_to_match est l'user steam avec lequel on calcule le score, c'est un SteamUser
    max_score est le score maximal que peut donner un jeu (si les paliers sont les mêmes)
    '''
    def score2(self, user_to_match, max_score=100):
        (good_games, _) = self.games_corresponding(user_to_match)
        score = 0
        for (_, _, p1, _, p2) in good_games:
            score += max_score * self.palier_dist(p1, p2)
        return (score, good_games)
    
        
    '''
    best_scores envoie la liste des users me correspondant le mieux, à partir d'une liste d'users
    '''
    def best_scores(self, list_users, max_score=100, nb_best=5):
        nb_results = 0
        list_results = []
        for user in list_users:
            (score, games) = self.score2(user, max_score)
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

    def score(self, user, max_score=100):
        return self.best_scores([user], max_score).pop()
    
    def friendlist(self):
        return self.steamuser.friends

    '''
    best_scores_file envoie la liste des users me correspondant le mieux, 
    à partir d'une liste d'users issue d'un fichier d'id
    '''
    def best_scores_file(self, name_file_id, max_score, nb_best=5):
        nb_results = 0
        list_results = []
        file_id = open(name_file_id, "r")
        for ligne in file_id:
            user = steamapi.user.SteamUser(int(ligne))
            (score, games) = self.score2(user, max_score)
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
            

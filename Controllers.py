from Models.Match import Match
from Models.Player import Player
from Models.Tournament import Tournament
from Models.Round import Round
import json
import random
from datetime import datetime

class Controllers:

    #===========================player controller===========================#
    def add_player_to_tournament(self, tournament, player):
        tournament.players.append(player)
        return tournament

    #===========================tournament controller===========================#
    def create_tournament(self, name, location, beginning_date, end_date, number_of_rounds=4, description=""):
        tournament = Tournament(
            name, 
            location, 
            beginning_date, 
            end_date, 
            number_of_rounds, 
            description
        )
        return tournament
    

    #=========================Match controller===============================#
    """
    Gère le contrôleur des scores
    """
    def set_score(self, score_1, score_2):
        """
        Attribut les scores d'un match
        """
        valid_scores = [0, 0.5, 1] 

        #Vérifie que les scores entrés soient valides
        if score_1 not in valid_scores or score_2 not in valid_scores:
            raise ValueError ("Score invalide: les scores doivent être 0, 0.5 ou 1")
        
        #Vérifie que les scores de tous le match soient entrés
        if score_1 + score_2 != 1:
            raise ValueError ("le score total du match doit être de 1 pour couvrir un gagnat + un perdant ou une égalité")

        self.score_1 = score_1
        self.score_2 = score_2
    
    def get_winner(self):
        """
        Déterminer le gagnant du match ou l'égalité
        """
        if self.score_1 > self.score_2:
            return f'{self.Player_1.first_name} gagne le match contre {self.Player_2.first_name}'
        elif self.score_1 < self.score_2:
            return f'{self.Player_2.first_name} gagne le match contre {self.Player_1.first_name}'
        else:
            return f'Égalité entre {self.player_1.first_name} et {self.player_2.first_name}'
        
    def is_completed(self):
        """
        Vérfifie qu'un match soit terminé
        """
        return self.score_1 != 0 or self.score_2 != 0
    
    def __str__(self):
        """"
        Représentation textuelle du match
        """
        status()
        if self.is_completed():
            status = "En attente"
        else:
            status = f'{self.player_1.first_name}{self.score_1} : {self.player_2.first_name}{self.score_2} / Match terminé'
  
    #===========================round controller===========================#
    """
    Gérer les rondes du tournoi
    """   

    def add_match_to_round(self, round_obj, match):
        """
        Ajoute un match au round.
        """
        if round_obj.is_completed:
            raise ValueError ("Impossible d'ajouter un match à un tour terminé")
        
        round_obj.match.append(match)
        return round_obj
       
    def create_first_round(self, tournament):
        """
        Gérer la première ronde.

        Ici les joueurs doivent s'affronter dans l'oredre 1vs2 et 3vs4 ou plus
        """
        if len(tournament.players) < 2:
            raise ValueError("Le nombre de joueurs est insuffisant pour créer un appariement.")
        
        if len(tournament.players) % 2 != 0:
            raise ValueError("Le nombre de joueurs n'est pas un nombre pair. Il est donc impossible de faire des appariements.")            

        #creer la première ronde
        first_round = Round(round_number=1)
        for i in range (0, len(tournament.players), 2):
            player_1 = tournament.players[i]
            player_2 = tournament.players[i + 1]
            match = Match(player_1, player_2)
            self.add_match_to_round(first_round, match)
        
        #ajouter la ronde au tournoi
        tournament.laps.append(first_round)
        tournament.actual_round += 1

        return first_round
    
    def next_round(self, tournament):
        """
        Gère les rondes à partir de la manche 2.
        """

        
  
       
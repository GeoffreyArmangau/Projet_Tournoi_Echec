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
            max_rounds=number_of_rounds, 
            description=description
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
    
    def match_to_dictionary(self):
        return {
            "player_1_name" : self.player1.last_name,
            "player_1_ID": self.player1.identification,
            "player_1_score": self.score1,
            "player_2_name" : self.player2.last_name,
            "player_2_ID": self.player2.identification,
            "player_2_score": self.score2
        }
    
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
        
        round_obj.matches.append(match)
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
        tournament.rounds.append(first_round)
        tournament.actual_round += 1

        return first_round
    
    def next_round(self, tournament):
        """
        Gère les rondes à partir de la manche 2.
        """
        
        if tournament.actual_round > tournament.max_rounds:
            raise ValueError ("Le nombre de round max est atteint")

        if not tournament.rounds == []:
            last_round = tournament.rounds[-1]

            for match in last_round.matches:
                if match.score1 == 0 and match.score2 == 0:
                    raise ValueError ("les matchs de la dernière ronde ne sont pas terminés")
        
        #récupération des scores avant tri
        total_player_scores = {}
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                total_player_scores[match.player1] = total_player_scores.get(match.player1, 0) + match.score1
                total_player_scores[match.player2] = total_player_scores.get(match.player2, 0) + match.score2
        
        #tri des joueurs avant la nouvelle ronde
        def get_score(player_score_pair):
            return player_score_pair[1]  # Retourne le score

        sorted_players = sorted(total_player_scores.items(), key=get_score, reverse=True)

        new_round = Round(round_number=1+tournament.actual_round)
        for i in range(0, len(sorted_players), 2):
            player_1 = sorted_players[i][0]     
            player_2 = sorted_players[i+1][0] 
            match = Match(player_1, player_2)
            self.add_match_to_round(new_round, match)
        
        #ajouter la ronde au tournoi
        tournament.rounds.append(new_round)
        tournament.actual_round += 1
        
        return new_round

from Models.Match import Match
from Models.Round import Round
import random

class RoundsController:
    def __init__(self):
        """Initialise le contrôleur des rondes"""
        pass

    def create_round(self, tournament, tournaments_controller):
        """
        Méthode générique pour créer un round (première ronde ou suivante)
        """
        if tournament.actual_round == 0:
            return self.create_first_round(tournament, tournaments_controller)
        else:
            return self.next_round(tournament, tournaments_controller)

    def add_match_to_round(self, round_obj, match):
        """
        Ajoute un match au round.
        """
        if round_obj.is_completed:
            raise ValueError("Impossible d'ajouter un match à un tour terminé")
        
        round_obj.matches.append(match)
        return round_obj
       
    def create_first_round(self, tournament, tournaments_controller):
        """
        Gérer la première ronde.

        Ici les joueurs doivent s'affronter dans l'ordre 1vs2 et 3vs4 ou plus
        """
        if len(tournament.players) < 2:
            raise ValueError("Le nombre de joueurs est insuffisant pour créer un appariement.")
        
        if len(tournament.players) % 2 != 0:
            raise ValueError("Le nombre de joueurs n'est pas un nombre pair. Il est donc impossible de faire des appariements.")            

        # Créer la première ronde
        first_round = Round(round_number=1)
        shuffled_players = tournament.players.copy()
        random.shuffle(shuffled_players)
        for i in range(0, len(shuffled_players), 2):
            player_1 = shuffled_players[i]
            player_2 = shuffled_players[i + 1]
            match = Match(player_1, player_2)
            self.add_match_to_round(first_round, match)
        
        # Ajouter la ronde au tournoi
        tournament.rounds.append(first_round)
        tournament.actual_round += 1
        
        # Sauvegarde automatique après création du round
        tournaments_controller.save_tournament_complete_to_json(tournament)

        return first_round
    
    def get_played_matches(self, tournament):
        """
        Retourne les appariements déjà joués
        """
        played_matches = set()
        for round_obj in tournament.rounds:  
            for match in round_obj.matches:  
                played_matches.add((match.player1, match.player2))
                played_matches.add((match.player2, match.player1))
        return played_matches
    
    def next_round(self, tournament, tournaments_controller):
        """
        Gère les rondes à partir de la manche 2.
        """
        
        if tournament.actual_round >= tournament.max_rounds:
            raise ValueError("Le nombre de round max est atteint")

        if tournament.rounds:
            last_round = tournament.rounds[-1]

            for match in last_round.matches:
                if match.score1 == 0 and match.score2 == 0:
                    raise ValueError("Les matchs de la dernière ronde ne sont pas terminés")
        
        # Récupération des scores avant tri
        total_player_scores = {}
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                total_player_scores[match.player1] = total_player_scores.get(match.player1, 0) + match.score1
                total_player_scores[match.player2] = total_player_scores.get(match.player2, 0) + match.score2
        
        # Tri des joueurs avant la nouvelle ronde, randomisation en cas d'égalité
        def get_score(player_score_pair):
            return (player_score_pair[1], random.random())  

        sorted_players = sorted(total_player_scores.items(), key=get_score, reverse=True)
        
        new_round = Round(round_number=tournament.actual_round + 1)
        played_matches = self.get_played_matches(tournament)
        
        # Récupérer la liste des joueurs classés
        available_players = []
        for player, score in sorted_players:
            available_players.append(player)

        # Appariement en évitant une rencontre double
        while len(available_players) >= 2:
            player_1 = available_players[0]
            for player in available_players[1:]:
                player_2 = player
                if (player_1, player_2) not in played_matches:             
                    match = Match(player_1, player_2)
                    self.add_match_to_round(new_round, match)
                    available_players.remove(player_1)
                    available_players.remove(player_2)
                    break
            else:
                raise ValueError("Aucun match disponible")
     
        # Ajouter la ronde au tournoi
        tournament.rounds.append(new_round)
        tournament.actual_round += 1
        
        # Sauvegarde automatique après création du round
        tournaments_controller.save_tournament_complete_to_json(tournament)
        
        return new_round

    def update_players_scores(self, tournament):
        """
        Met à jour les scores totaux des joueurs dans le tournoi
        """
        # Réinitialiser les scores
        for player in tournament.players:
            player.tournament_score = 0
        
        # Calculer les nouveaux scores
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                match.player1.tournament_score += match.score1
                match.player2.tournament_score += match.score2

    def get_round_result(self, round_obj):
        """
        Retourne les résultats du tour sous forme de dictionnaire
        """
        matches_results = []
        for match in round_obj.matches:
            match_result = {
                "player1": f"{match.player1.first_name} {match.player1.last_name}",
                "player1_color": match.player1_color,
                "player2": f"{match.player2.first_name} {match.player2.last_name}",
                "player2_color": match.player2_color,
                "score1": match.score1,
                "score2": match.score2
            }
            matches_results.append(match_result)
        
        return {
            "round_name": round_obj.name,
            "matches": matches_results,
            "is_completed": round_obj.is_completed
        }

class MatchesController:
    def __init__(self):
        """Initialise le contrôleur des matches"""
        pass

    def set_score(self, score_1, score_2):
        """
        Attribut les scores d'un match
        """
        valid_scores = [0, 0.5, 1] 

        # Vérifie que les scores entrés soient valides
        if score_1 not in valid_scores or score_2 not in valid_scores:
            raise ValueError("Score invalide: les scores doivent être 0, 0.5 ou 1")
        
        # Vérifie que les scores de tous le match soient entrés
        if score_1 + score_2 != 1:
            raise ValueError("le score total du match doit être de 1 pour couvrir un gagnant + un perdant ou une égalité")

        return True
    
    def get_winner(self, match):
        """
        Déterminer le gagnant du match ou l'égalité
        """
        if match.score1 > match.score2:
            return f'{match.player1.first_name} gagne le match contre {match.player2.first_name}'
        elif match.score1 < match.score2:
            return f'{match.player2.first_name} gagne le match contre {match.player1.first_name}'
        else:
            return f'Égalité entre {match.player1.first_name} et {match.player2.first_name}'
        
    def is_completed(self, match):
        """
        Vérifie qu'un match soit terminé
        """
        return match.score1 != 0 or match.score2 != 0
    
    def match_to_dictionary(self, match):
        """
        Retourne le match sous forme de dictionnaire
        """
        return {
            "player_1_name": match.player1.last_name,
            "player_1_ID": match.player1.identification,
            "player_1_score": match.score1,
            "player_2_name": match.player2.last_name,
            "player_2_ID": match.player2.identification,
            "player_2_score": match.score2
        }
    
    def get_match_status(self, match):
        """
        Représentation textuelle du statut du match
        """
        if self.is_completed(match):
            return f'{match.player1.first_name} {match.score1} : {match.player2.first_name} {match.score2} / Match terminé'
        else:
            return "En attente"

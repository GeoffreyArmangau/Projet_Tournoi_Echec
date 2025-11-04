class Match:
    """
    Un match unique stocké sous forme de tuple contenant deux listes.
    Chaque liste contient [joueur, score].
    """
    def __init__(self, player1, player2, score1=0, score2=0):
        """
        Initialise un match entre deux joueurs.
       
        """
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
    
    def get_match_tuple(self):
        """
        Retourne le match sous forme de tuple contenant deux listes.
        Format: ([joueur1, score1], [joueur2, score2])
        """
        return ([self.player1, self.score1], [self.player2, self.score2])
    
    def Match_Dictionary(self):
        """
        Retourne le match sous forme de dictionnaire pour JSON
        """
        return {
            "player1_id": self.player1.identification,
            "player1_name": f"{self.player1.first_name} {self.player1.last_name}",
            "player2_id": self.player2.identification,
            "player2_name": f"{self.player2.first_name} {self.player2.last_name}",
            "score1": self.score1,
            "score2": self.score2
        }
   
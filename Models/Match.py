import random


class Match:
    """
    Un match unique stocké sous forme de tuple contenant deux listes.
    Chaque liste contient [joueur, score].
    """

    def __init__(
            self,
            player1,
            player2,
            score1=0,
            score2=0,
            player1_color=None,
            player2_color=None):
        """
        Initialise un match entre deux joueurs.
        Les couleurs sont attribuées aléatoirement si non spécifiées.
        """
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

        # Attribution des couleurs
        if player1_color and player2_color:
            self.player1_color = player1_color
            self.player2_color = player2_color
        else:
            # Attribution aléatoire des couleurs
            if random.choice([True, False]):
                self.player1_color = "Blanc"
                self.player2_color = "Noir"
            else:
                self.player1_color = "Noir"
                self.player2_color = "Blanc"

    def get_match_tuple(self):
        """
        Retourne le match sous forme de tuple contenant deux listes.
        Format: ([joueur1, score1], [joueur2, score2])
        """
        return ([self.player1, self.score1], [self.player2, self.score2])

    def get_match_display(self):
        """
        Retourne l'affichage formaté du match avec les couleurs
        """
        player1_display = f"{
            self.player1.first_name} {
            self.player1.last_name} ({
            self.player1_color})"
        player2_display = f"{
            self.player2.first_name} {
            self.player2.last_name} ({
            self.player2_color})"
        return f"{player1_display} vs {player2_display}"

    def Match_Dictionary(self):
        """
        Retourne le match sous forme de dictionnaire pour JSON
        """
        return {
            "player1_id": self.player1.identification,
            "player1_name": f"{
                self.player1.first_name} {
                self.player1.last_name}",
            "player1_color": self.player1_color,
            "player2_id": self.player2.identification,
            "player2_name": f"{
                self.player2.first_name} {
                    self.player2.last_name}",
            "player2_color": self.player2_color,
            "score1": self.score1,
            "score2": self.score2}

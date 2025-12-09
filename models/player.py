class Player:
    """
    Modélise un joueur d'échecs avec ses informations personnelles et son score de tournoi.
    """
    def __init__(
            self,
            first_name,
            last_name,
            date_of_birth,
            age,
            identification):
        """
        Initialise un joueur avec nom, prénom, date de naissance, âge, identifiant et score de tournoi.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.identification = identification
        self.tournament_score = 0

    def Player_Dictionary(self):
        """
        Retourne un dictionnaire représentant le joueur pour la sérialisation JSON.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "age": self.age,
            "identification": self.identification,
            "tournament_score": getattr(self, 'tournament_score', 0)
        }

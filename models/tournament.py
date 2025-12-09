class Tournament:
    """
    Représente un tournoi d'échecs avec ses informations, rounds et joueurs.
    """
    def __init__(
            self,
            name,
            location,
            beginning_date,
            end_date,
            max_rounds=4,
            actual_round=0,
            rounds=[],
            players=[],
            description=""):
        """
        Initialise un tournoi avec nom, lieu, dates, rounds, joueurs et description.
        """
        self.name = name
        self.location = location
        self.beginning_date = beginning_date
        self.end_date = end_date
        self.max_rounds = max_rounds
        self.actual_round = actual_round
        self.rounds = rounds
        self.players = players
        self.description = description

    def Tournament_Dictionary(self):
        """
        Retourne un dictionnaire représentant le tournoi pour la sérialisation JSON.
        """
        return {
            "name": self.name,
            "location": self.location,
            "beginning_date": self.beginning_date,
            "end_date": self.end_date,
            "max_rounds": self.max_rounds,
            "actual_round": self.actual_round,
            "rounds": [
                round_obj.Round_Dictionary() for round_obj in self.rounds],
            "players": [
                player.Player_Dictionary() for player in self.players],
            "description": self.description}

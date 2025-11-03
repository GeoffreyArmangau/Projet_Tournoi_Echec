class Tournament:
    def __init__(self, name, location, beginning_date, end_date, round = 4, actual_round=0, rounds = [], players = [], description=""):
        self.name = name
        self.location = location
        self.beginning_date = beginning_date
        self.end_date = end_date
        self.round = round
        self.actual_round = actual_round
        self.rounds = rounds
        self.players = players
        self.description = description

    def Tournament_Dictionary(self):
        return {
            "name": self.name,
            "location": self.location,
            "beginning_date": self.beginning_date,
            "end_date": self.end_date,
            "round": self.round,
            "actual_round": self.actual_round,
            "rounds": [round.round_to_dict() for round in self.rounds],
            "players": [player.Player_Dictionary() for player in self.players],
            "description": self.description
        }
    
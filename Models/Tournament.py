class Tournament:
    def __init__(self, name, location, beginning_date, end_date, max_rounds = 4, actual_round=0, rounds = [], players = [], description=""):
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
        return {
            "name": self.name,
            "location": self.location,
            "beginning_date": self.beginning_date,
            "end_date": self.end_date,
            "round": self.max_rounds,
            "actual_round": self.actual_round,
            "rounds": [round_obj.round_to_dict() for round_obj in self.rounds],
            "players": [player.Player_Dictionary() for player in self.players],
            "description": self.description
        }
    
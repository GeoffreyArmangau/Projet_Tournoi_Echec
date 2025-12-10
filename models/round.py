class Round:
    """
    Représente une ronde (tour) d'un tournoi d'échecs, avec ses matches et son état.
    """
    def __init__(self, round_number=1, matches=None):
        """
        Initialise une ronde avec un numéro, une liste de matches et des informations de statut.
        """
        self.name = f'Ronde n°{round_number}'
        self.matches = matches if matches is not None else []
        self.start_datetime = None
        self.end_datetime = None
        self.is_started = False
        self.is_completed = False

    def Round_Dictionary(self):
        """
        Retourne un dictionnaire représentant la ronde pour la sérialisation JSON.
        """
        return {
            "name": self.name,
            "matches": [match.Match_Dictionary() for match in self.matches],
            "start_datetime": self.start_datetime.strftime("%d/%m/%Y %H:%M:%S") if self.start_datetime else None,
            "end_datetime": self.end_datetime.strftime("%d/%m/%Y %H:%M:%S") if self.end_datetime else None,
            "is_started": self.is_started,
            "is_completed": self.is_completed
        }

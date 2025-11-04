class Round:
    def __init__(self, round_number = 1, matches=None):
        """
        Initialise un tour.
               
        """
        
        self.name = f'Ronde n°{round_number}'
        self.matches = matches if matches is not None else []
        self.start_datetime = None
        self.end_datetime = None
        self.is_started = False
        self.is_completed = False
    
    def Round_Dictionary(self):
        """
        Retourne le round sous forme de dictionnaire pour JSON
        """
        return {
            "name": self.name,
            "matches": [match.Match_Dictionary() for match in self.matches],
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "is_started": self.is_started,
            "is_completed": self.is_completed
        }
    
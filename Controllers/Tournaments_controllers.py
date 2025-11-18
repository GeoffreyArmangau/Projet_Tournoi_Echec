from Models.Tournament import Tournament
import json


class TournamentsController:
    def __init__(self):
        """Initialise la liste pour stocker les tournois"""
        self.tournaments = []

    def create_tournament(
            self,
            name,
            location,
            beginning_date,
            end_date,
            number_of_rounds=4,
            description=""):
        """Crée un nouveau tournoi"""
        tournament = Tournament(
            name,
            location,
            beginning_date,
            end_date,
            max_rounds=number_of_rounds,
            description=description
        )
        return tournament

    def save_all_tournaments_to_json(self):
        """Sauvegarde tous les tournois dans tournaments.json"""
        tournaments_data = []

        for t in self.tournaments:
            tournament_dict = {
                "name": t.name,
                "location": t.location,
                "beginning_date": t.beginning_date,
                "end_date": t.end_date,
                "max_rounds": t.max_rounds,
                "actual_round": t.actual_round,
                "description": t.description,
                "players_count": len(t.players),
                "rounds_count": len(t.rounds)
            }
            tournaments_data.append(tournament_dict)

        with open('tournaments.json', 'w') as file:
            json.dump(tournaments_data, file, indent=4)

    def save_tournament_to_json(self, tournament):
        """Sauvegarde un tournoi - utilise la méthode globale"""
        self.save_all_tournaments_to_json()

    def load_tournaments_from_json(self):
        """Charge tous les tournois depuis tournaments.json"""
        try:
            with open('tournaments.json', 'r') as file:
                tournaments_data = json.load(file)
                tournaments = []
                for tournament_data in tournaments_data:
                    tournament = Tournament(
                        name=tournament_data['name'],
                        location=tournament_data['location'],
                        beginning_date=tournament_data['beginning_date'],
                        end_date=tournament_data['end_date'],
                        max_rounds=tournament_data['max_rounds'],
                        actual_round=tournament_data['actual_round'],
                        description=tournament_data['description']
                    )
                    tournaments.append(tournament)
                return tournaments
        except FileNotFoundError:
            return []

    def save_tournament_complete_to_json(self, tournament):
        """Sauvegarde complète d'un tournoi avec rounds, matches et joueurs"""
        try:
            # Charger les tournois existants
            try:
                with open('tournaments_complete.json', 'r') as file:
                    tournaments = json.load(file)
            except FileNotFoundError:
                tournaments = []

            # Vérifier si le tournoi existe déjà et le mettre à jour
            tournament_found = False
            for i, existing_tournament in enumerate(tournaments):
                if existing_tournament['name'] == tournament.name:
                    tournaments[i] = tournament.Tournament_Dictionary()
                    tournament_found = True
                    break

            # Si le tournoi n'existe pas, l'ajouter
            if not tournament_found:
                tournaments.append(tournament.Tournament_Dictionary())

            # Sauvegarder
            with open('tournaments_complete.json', 'w') as file:
                json.dump(tournaments, file, indent=4)

            return True, "Tournoi sauvegardé avec succès"

        except Exception as e:
            return False, f"Erreur lors de la sauvegarde: {e}"

    def load_tournament_complete_from_json(self, tournament_name):
        """Charge un tournoi complet depuis JSON par son nom"""
        try:
            with open('tournaments_complete.json', 'r') as file:
                tournaments_data = json.load(file)

            for tournament_data in tournaments_data:
                if tournament_data['name'] == tournament_name:
                    # Reconstruire les joueurs
                    from Models.Player import Player
                    players = []
                    for player_data in tournament_data['players']:
                        player = Player(
                            player_data['first_name'],
                            player_data['last_name'],
                            player_data['date_of_birth'],
                            player_data['age'],
                            player_data['identification']
                        )
                        players.append(player)

                    # Créer le tournoi
                    tournament = Tournament(
                        name=tournament_data['name'],
                        location=tournament_data['location'],
                        beginning_date=tournament_data['beginning_date'],
                        end_date=tournament_data['end_date'],
                        max_rounds=tournament_data['max_rounds'],
                        actual_round=tournament_data['actual_round'],
                        rounds=[],  # On va reconstruire les rounds
                        players=players,
                        description=tournament_data['description']
                    )

                    # Reconstruire les rounds et matches
                    from Models.Round import Round
                    from Models.Match import Match
                    for round_data in tournament_data['rounds']:
                        # Créer le round
                        round_obj = Round()
                        round_obj.name = round_data['name']
                        round_obj.start_datetime = round_data['start_datetime']
                        round_obj.end_datetime = round_data['end_datetime']
                        round_obj.is_started = round_data['is_started']
                        round_obj.is_completed = round_data['is_completed']

                        # Reconstruire les matches
                        for match_data in round_data['matches']:
                            # Trouver les joueurs par ID
                            player1 = next(
                                (p for p in players if p.identification ==
                                 match_data['player1_id']), None)
                            player2 = next(
                                (p for p in players if p.identification ==
                                 match_data['player2_id']), None)

                            if player1 and player2:
                                # Récupérer les couleurs depuis les données
                                # JSON si disponibles
                                player1_color = match_data.get(
                                    'player1_color', None)
                                player2_color = match_data.get(
                                    'player2_color', None)
                                match = Match(
                                    player1,
                                    player2,
                                    match_data['score1'],
                                    match_data['score2'],
                                    player1_color,
                                    player2_color)
                                round_obj.matches.append(match)

                        tournament.rounds.append(round_obj)

                    return tournament

            return None

        except FileNotFoundError:
            return None

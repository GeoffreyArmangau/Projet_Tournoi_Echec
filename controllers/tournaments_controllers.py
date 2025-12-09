from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player
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
                        rounds=[],
                        players=players,
                        description=tournament_data['description']
                    )

                    # Reconstruire les rounds et matches
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

    def manage_tournaments(self, view, players_controller, rounds_controller):
        while True:
            view.display_tournaments_menu()
            choice = input("votre choix (1-6): ")
            if choice == "1":
                self.create_new_tournament(view)
            elif choice == "2":
                self.display_tournament(view)
            elif choice == "3":
                self.register_players_to_tournament(view, players_controller)
            elif choice == "4":
                self.launch_tournament(view, rounds_controller)
            elif choice == "6":
                break
            else:
                view.display_message("Choix invalide")
            input("Appuyez sur Entrée pour continuer...")

    def create_new_tournament(self, view):
        view.display_message("=== Création d'un nouveau tournoi ===")
        (name, location, beginning_date, end_date, number_of_rounds, description) = view.get_tournament_info()
        tournament = self.create_tournament(name, location, beginning_date,
                                            end_date, int(number_of_rounds), description)
        self.tournaments.append(tournament)
        self.save_tournament_to_json(tournament)
        view.display_message(f"Tournoi '{name}' créé avec succès !")

    def display_tournament(self, view):
        view.display_message("=== Liste des tournois ===")
        if self.tournaments:
            for i, tournament in enumerate(self.tournaments):
                print(f"{i + 1}. {tournament.name}")
                print(f"Se déroulera à {tournament.location}")
                print(
                    f"Le tournoi enregistre {len(tournament.players)} joueurs, "
                    f"qui s'affronterons sur {tournament.max_rounds} rondes."
                )
                print(f"{tournament.description}")
        else:
            view.display_message("Aucun tournoi de crée pour le moment")

    def register_players_to_tournament(self, view, players_controller):
        if not self.tournaments:
            view.display_message("Aucun tournoi créé")
            return

        if not players_controller.players:
            view.display_message("Aucun joueur créé")
            return

        print("=== Sélection du tournoi ===")
        for i, tournament in enumerate(self.tournaments):
            print(f"{i + 1}. {tournament.name} ({len(tournament.players)} joueurs inscrits)")
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.tournaments[tournament_index]
        print("\n=== Joueurs disponibles ===")

        for i, player in enumerate(players_controller.players):
            print(f"{i + 1}. {player.first_name} {player.last_name} ({player.identification})")
        player_choice = input("Choisissez le numéro du joueur à inscrire: ")
        player_index = int(player_choice) - 1
        selected_player = players_controller.players[player_index]
        success, message = players_controller.add_player_to_tournament(selected_tournament, selected_player)
        view.display_message(message)

    def launch_tournament(self, view, rounds_controller):
        if not self.tournaments:
            view.display_message("Aucun tournoi disponible.")
            return
        print("=== Sélection du tournoi à lancer ===")
        for i, tournament in enumerate(self.tournaments):
            print(f"{i + 1}. {tournament.name} ({len(tournament.players)} joueurs)")
        choice = input("Numéro du tournoi à lancer : ")

        try:
            idx = int(choice) - 1
            tournament = self.tournaments[idx]
        except (ValueError, IndexError):
            view.display_message("Numéro de tournoi invalide.")
            return
        if len(tournament.players) < 2:
            view.display_message("Pas assez de joueurs inscrits pour lancer le tournoi.")
            return
        if tournament.actual_round >= tournament.max_rounds:
            view.display_message("Ce tournoi est déjà terminé.")
            return
        while tournament.actual_round < tournament.max_rounds:
            round_number = tournament.actual_round + 1
            print(f"\n=== Lancement de la ronde {round_number} ===")
            # Utilisation du RoundsController pour générer le round et les appariements
            if tournament.actual_round == 0:
                round_obj = rounds_controller.create_first_round(tournament, self)
            else:
                round_obj = rounds_controller.next_round(tournament, self)

            # Saisie des scores pour chaque match
            for match in round_obj.matches:
                print(
                    f"Match : {match.player1.first_name} {match.player1.last_name} vs "
                    f"{match.player2.first_name} {match.player2.last_name}"
                )
                score1, score2 = self.get_scores_input(match.player1, match.player2)
                match.score1 = score1
                match.score2 = score2

            # Marquer le round comme terminé et renseigner la date/heure de fin
            rounds_controller.mark_round_completed(round_obj)
            print(f"Ronde {round_number} terminée.")
            self.save_tournament_complete_to_json(tournament)
        print(f"Tournoi '{tournament.name}' terminé !")
        print("=== Sélection du tournoi à lancer ===")
        for i, tournament in enumerate(self.tournaments):
            print(f"{i + 1}. {tournament.name} ({len(tournament.players)} joueurs)")
        choice = input("Numéro du tournoi à lancer : ")

        try:
            idx = int(choice) - 1
            tournament = self.tournaments[idx]
        except (ValueError, IndexError):
            view.display_message("Numéro de tournoi invalide.")
            return
        if len(tournament.players) < 2:
            view.display_message("Pas assez de joueurs inscrits pour lancer le tournoi.")
            return
        if tournament.actual_round >= tournament.max_rounds:
            view.display_message("Ce tournoi est déjà terminé.")
            return
        while tournament.actual_round < tournament.max_rounds:
            round_number = tournament.actual_round + 1
            print(f"\n=== Lancement de la ronde {round_number} ===")
            matches = self._generate_pairings(tournament)
            if not matches:
                print("Impossible de générer de nouveaux appariements sans doublon.")
                break
            for player1, player2 in matches:
                print(
                    f"Match : {player1.first_name} {player1.last_name} vs "
                    f"{player2.first_name} {player2.last_name}"
                )
                score1, score2 = self.get_scores_input(player1, player2)
                match_obj = Match(player1, player2, score1, score2)
                if tournament.actual_round < len(tournament.rounds):
                    round_obj = tournament.rounds[tournament.actual_round]
                else:
                    round_obj = Round(round_number)
                    tournament.rounds.append(round_obj)
                round_obj.matches.append(match_obj)
            round_obj.is_completed = True
            tournament.actual_round += 1
            print(f"Ronde {round_number} terminée.")
            self.save_tournament_complete_to_json(tournament)
        print(f"Tournoi '{tournament.name}' terminé !")

    def get_scores_input(self, player1, player2):
        while True:
            try:
                score1 = float(input(f"Score pour {player1.first_name} {player1.last_name} (0, 0.5 ou 1): "))
                if score1 not in (0, 0.5, 1):
                    print("Score invalide. Entrez 0, 0.5 ou 1.")
                    continue
                if score1 == 0.5:
                    score2 = 0.5
                elif score1 == 1:
                    score2 = 0
                elif score1 == 0:
                    score2 = 1
                print(f"Score pour {player2.first_name} {player2.last_name} : {score2}")
                return score1, score2
            except ValueError:
                print("Entrée invalide. Entrez un nombre.")

    def _generate_pairings(self, tournament):
        played = set()
        for rnd in tournament.rounds:
            for match in rnd.matches:
                ids = tuple(sorted([match.player1.identification, match.player2.identification]))
                played.add(ids)
        import random
        players = tournament.players[:]
        if tournament.actual_round == 0:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: getattr(p, 'tournament_score', 0), reverse=True)
        pairings = []
        used = set()
        for i, player1 in enumerate(players):
            if player1 in used:
                continue
            for j, player2 in enumerate(players):
                if i != j and player2 not in used:
                    ids = tuple(sorted([player1.identification, player2.identification]))
                    if ids not in played:
                        pairings.append((player1, player2))
                        used.add(player1)
                        used.add(player2)
                        break
        return pairings

    def get_score_input(self, player):
        while True:
            try:
                score = float(input(f"Score pour {player.first_name} {player.last_name} (0, 0.5 ou 1): "))
                if score in (0, 0.5, 1):
                    return score
                else:
                    print("Score invalide. Entrez 0, 0.5 ou 1.")
            except ValueError:
                print("Entrée invalide. Entrez un nombre.")

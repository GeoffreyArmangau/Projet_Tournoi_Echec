from models.player import Player
import json
from datetime import datetime


class PlayersController:
    def __init__(self):
        """
        Initialise le contrôleur des joueurs et la liste des joueurs.
        """
        self.players = []

    def create_player_simple(
            self,
            first_name,
            last_name,
            date_of_birth,
            national_id):
        """
        Crée un nouveau joueur avec les informations fournies et l'ajoute à la liste.
        Retourne un tuple (succès, message).
        """
        try:
            # Validation des champs vides
            if not all([first_name, last_name, date_of_birth, national_id]):
                return False, "Tous les champs sont obligatoires !"

            current_year = datetime.now().year
            birth_year = int(date_of_birth.split('/')[2])
            age = current_year - birth_year

            player = Player(
                first_name,
                last_name,
                date_of_birth,
                age,
                national_id)
            self.players.append(player)

            # Sauvegarde automatique
            self.save_player_to_json(player)

            return True, f"Joueur {first_name} {last_name} créé avec succès !"

        except Exception as e:
            return False, f"Erreur lors de la création: {e}"

    def add_player_to_tournament(self, tournament, player):
        """
        Ajoute un joueur à la liste des joueurs d'un tournoi si non déjà inscrit.
        Retourne un tuple (succès, message).
        """
        # Vérifier que le joueur n'est pas déjà dans le tournoi
        for existing_player in tournament.players:
            if existing_player.identification == player.identification:
                return False, f"Le joueur {
                    player.first_name} {
                    player.last_name} est déjà inscrit à ce tournoi"

        tournament.players.append(player)

        return True, f"Joueur {
            player.first_name} {
            player.last_name} ajouté avec succès"

    def save_player_to_json(self, player):
        """
        Sauvegarde un joueur dans le fichier players.json (format JSON).
        """
        try:
            with open('players.json', 'r') as file:
                players = json.load(file)
        except FileNotFoundError:
            players = []

        players.append(player.Player_Dictionary())

        with open('players.json', 'w') as file:
            json.dump(players, file, indent=4)

    def load_players_from_json(self):
        """
        Charge tous les joueurs depuis le fichier players.json et retourne une liste de Player.
        """
        try:
            with open('players.json', 'r') as file:
                players_data = json.load(file)
                players = []
                for player_data in players_data:
                    player = Player(
                        player_data['first_name'],
                        player_data['last_name'],
                        player_data['date_of_birth'],
                        player_data['age'],
                        player_data['identification']
                    )
                    # Charger le tournament_score s'il existe dans les données
                    player.tournament_score = player_data.get(
                        'tournament_score', 0)
                    players.append(player)
                return players
        except FileNotFoundError:
            return []

    def manage_players(self, view):
        """
        Affiche le sous-menu de gestion des joueurs et gère les actions utilisateur.
        """
        while True:
            view.display_submenu("Joueurs")
            choice = input("Votre choix (1-5): ")
            if choice == "1":
                self.create_player(view)
            elif choice == "2":
                self.display_players(view)
            elif choice == "3":
                self.players = self.load_players_from_json()
                view.display_message("Joueurs chargés depuis le fichier JSON")
            elif choice == "4":
                for player in self.players:
                    self.save_player_to_json(player)
                view.display_message(
                    "Tous les joueurs sauvegardés dans le fichier JSON")
            elif choice == "5":
                break
            else:
                view.display_message("Choix invalide")
            input("Appuyez sur Entrée pour continuer...")

    def create_player(self, view):
        """
        Lance la procédure de création d'un nouveau joueur via la vue.
        """
        view.display_message(
            "=== Création d'un nouveau joueur ===")
        first_name, last_name, date_of_birth, national_id = view.get_player_info()
        success, message = self.create_player_simple(first_name, last_name, date_of_birth, national_id)
        view.display_message(message)

    def display_players(self, view):
        """
        Affiche la liste des joueurs enregistrés dans le contrôleur.
        """
        view.display_message("=== Liste des joueurs ===")
        if self.players:
            for i, player in enumerate(self.players):
                print(f"{i + 1}. {player.first_name} {player.last_name}")
                print(f"Né le: {player.date_of_birth} (âge: {player.age})")
                print(f"ID: {player.identification}")
                print()
        else:
            view.display_message("Aucun joueur créé pour le moment.")

class PlayersViews:
    def __init__(self, players_controller):
        self.players_controller = players_controller

    def get_player_info(self):
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (DD/MM/YYYY): ")
        national_id = input("ID national: ")
        return first_name, last_name, birth_date, national_id

    def manage_players(self):
        while True:
            self.display_submenu("Joueurs")
            choice = input("Votre choix (1-5): ")

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.display_players()
            elif choice == "3":
                self.players_controller.players = (
                    self.players_controller.load_players_from_json())
                self.display_message("Joueurs chargés depuis le fichier JSON")
            elif choice == "4":
                for player in self.players_controller.players:
                    self.players_controller.save_player_to_json(player)
                self.display_message(
                    "Tous les joueurs sauvegardés dans le fichier JSON")
            elif choice == "5":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")

    def create_player(self):
        self.display_message("=== Création d'un nouveau joueur ===")

        first_name, last_name, birth_date, national_id = self.get_player_info()

        if self.players_controller:
            success, message = self.players_controller.create_player_simple(
                first_name, last_name, birth_date, national_id)
            self.display_message(message)
        else:
            self.display_message("Players controller non disponible")

    def display_players(self):
        self.display_message("=== Liste des joueurs ===")

        if self.players_controller and self.players_controller.players:
            for i in range(len(self.players_controller.players)):
                player = self.players_controller.players[i]
                print(f"{i + 1}. {player.first_name} {player.last_name}")
                print(f"Né le: {player.date_of_birth} (âge: {player.age})")
                print(f"ID: {player.identification}")
                print()
        else:
            self.display_message("Aucun joueur créé pour le moment.")

    def display_message(self, message):
        print(message)

    def display_submenu(self, entity_name):
        """ Sous-menu de gestion des joueurs et tournois"""
        print(f"=== Gestion des {entity_name} ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Charger")
        print("4. Sauvegarder")
        print("5. Retour au menu principal")

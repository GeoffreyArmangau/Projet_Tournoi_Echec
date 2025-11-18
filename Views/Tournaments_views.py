class TournamentsViews:
    def __init__(
            self,
            tournaments_controller,
            players_controller,
            rounds_controller):
        self.tournaments_controller = tournaments_controller
        self.players_controller = players_controller
        self.rounds_controller = rounds_controller

    def display_tournaments_menu(self):
        """Menu spécialisé pour la gestion des tournois"""
        print("=== Gestion des Tournois ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Inscrire des joueurs")
        print("4. Lancer un tournoi")
        print("6. Retour au menu principal")

    def get_tournament_info(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        beginning_date = input("Date de début (DD/MM/YYYY): ")
        end_date = input("Date de fin (DD/MM/YYYY): ")
        number_of_rounds = input("Nombre de rondes: ")
        description = input("Description du tournoi: ")
        return name, location, beginning_date, end_date, number_of_rounds, description

    def manage_tournaments(self):
        while True:
            self.display_tournaments_menu()
            choice = input("votre choix (1-6): ")

            if choice == "1":
                self.create_new_tournament()
            elif choice == "2":
                self.display_tournament()
            elif choice == "3":
                self.register_players_to_tournament()
            elif choice == "4":
                self.launch_tournament()
            elif choice == "6":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")

    def create_new_tournament(self):
        self.display_message("=== Création d'un nouveau tournoi ===")

        (name, location, beginning_date, end_date,
         number_of_rounds, description) = self.get_tournament_info()
        if self.tournaments_controller:
            tournament = self.tournaments_controller.create_tournament(
                name, location, beginning_date, end_date,
                int(number_of_rounds), description)
            self.tournaments_controller.tournaments.append(tournament)

            self.tournaments_controller.save_tournament_to_json(tournament)

            self.display_message(f"Tournoi '{name}' créé avec succès !")
        else:
            self.display_message("Tournaments controller non disponible")

    def display_tournament(self):
        self.display_message("=== Liste des tournois ===")

        if self.tournaments_controller and self.tournaments_controller.tournaments:
            for i in range(len(self.tournaments_controller.tournaments)):
                tournament = self.tournaments_controller.tournaments[i]
                print(f"{i + 1}. {tournament.name}")
                print(f"Se déroulera à {tournament.location}")
                print(
                    f"Le tournoi enregistre {
                        len(
                            tournament.players)} joueurs, qui s'affronterons sur {
                        tournament.max_rounds} rondes.")
                print(f"{tournament.description}")
        else:
            self.display_message("Aucun tournoi de crée pour le moment")

    def register_players_to_tournament(self):
        """Inscrire des joueurs à un tournoi"""
        if not self.tournaments_controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return

        if not self.players_controller.players:
            self.display_message("Aucun joueur créé")
            return

        # Sélection du tournoi
        print("=== Sélection du tournoi ===")
        for i in range(len(self.tournaments_controller.tournaments)):
            tournament = self.tournaments_controller.tournaments[i]
            print(
                f"{i + 1}. {tournament.name} "
                f"({len(tournament.players)} joueurs inscrits)")

        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.tournaments_controller.tournaments[tournament_index]

        # Sélection des joueurs
        print("\n=== Joueurs disponibles ===")
        for i in range(len(self.players_controller.players)):
            player = self.players_controller.players[i]
            print(
                f"{i + 1}. {player.first_name} {player.last_name} "
                f"({player.identification})")

        player_choice = input("Choisissez le numéro du joueur à inscrire: ")
        player_index = int(player_choice) - 1
        selected_player = self.players_controller.players[player_index]

        # Ajouter le joueur au tournoi via le controller
        success, message = self.players_controller.add_player_to_tournament(
            selected_tournament, selected_player)
        self.display_message(message)

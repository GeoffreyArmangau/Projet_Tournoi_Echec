class MainViews:
    def __init__(
            self,
            players_controller,
            tournaments_controller,
            matches_controller,
            rounds_controller,
            reports_controller):
        """
        Initialise la vue principale avec les contrôleurs spécialisés
        """
        self.players_controller = players_controller
        self.tournaments_controller = tournaments_controller
        self.matches_controller = matches_controller
        self.rounds_controller = rounds_controller
        self.reports_controller = reports_controller

    def display_header(self):
        """
        Affiche l'en-tête principal du menu du système de tournoi d'échecs.
        """
        print("=" * 50)
        print("           SYSTÈME DE TOURNOI D'ÉCHECS           ")
        print("=" * 50)

    def display_menu(self):
        """
        Affiche le menu principal avec les différentes options disponibles.
        """
        print("1. Gestion des Joueurs")
        print("2. Gestion des Tournois")
        print("3. Rapports")
        print("4. Quitter")

    def get_user_choice(self):
        """
        Demande à l'utilisateur de choisir une option du menu principal et valide l'entrée.
        Retourne le choix sous forme de chaîne.
        """
        choice = input("Veuillez choisir l'une des options ci-dessus: ")
        choice = choice.strip()
        if choice and choice[0].isdigit():
            choice = choice[0]
        valid_choice = ["1", "2", "3", "4"]
        if choice not in valid_choice:
            raise ValueError(
                "Votre entrée n'est pas valide. "
                "Merci de rentrer un choix entre 1 et 4.")
        return choice

    def handle_choice(
            self,
            choice,
            players_views,
            tournaments_views,
            reports_views):
        """
        Exécute l'action correspondant au choix de l'utilisateur dans le menu principal.
        """
        if choice == "1":
            self.players_controller.manage_players(players_views)
        elif choice == "2":
            self.tournaments_controller.manage_tournaments(
                tournaments_views,
                self.players_controller,
                self.rounds_controller)
        elif choice == "3":
            self.reports_controller.manage_reports(
                reports_views,
                self.tournaments_controller,
                self.players_controller)
        elif choice == "4":
            print("Merci d'avoir utilisé le système de tournoi d'échecs. Au revoir!")
            exit()

    def display_message(self, message):
        """
        Affiche un message générique à l'utilisateur.
        """
        print(message)

    def display_submenu(self, entity_name):
        """
        Affiche un sous-menu pour la gestion d'une entité (joueurs ou tournois).
        """
        print(f"=== Gestion des {entity_name} ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Charger")
        print("4. Sauvegarder")
        print("5. Retour au menu principal")

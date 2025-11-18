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
        """ Gérer l'en-tête du menu"""
        print("=" * 50)
        print("           SYSTÈME DE TOURNOI D'ÉCHECS           ")
        print("=" * 50)

    def display_menu(self):
        """ Menu principal du programme """
        print("1. Gestion des Joueurs")
        print("2. Gestion des Tournois")
        print("3. Rapports")
        print("4. Quitter")

    def get_user_choice(self):
        choice = input("Veuillez choisir l'une des options ci-dessus: ")

        # Nettoyer l'input en gardant seulement le premier caractère s'il est
        # un chiffre
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
        if choice == "1":
            players_views.manage_players()
        elif choice == "2":
            tournaments_views.manage_tournaments()
        elif choice == "3":
            reports_views.manage_reports()
        elif choice == "4":
            print("Merci d'avoir utilisé le système de tournoi d'échecs. Au revoir!")
            exit()

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

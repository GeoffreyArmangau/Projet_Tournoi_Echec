from Controllers import Tournament

class View:
    def __init__(self, controller=None):
        self.controller = controller

    def display_header(self):
        """ Gérer l'en-tête du menu"""

        print("=" * 50)
        print("           SYSTÈME DE TOURNOI D'ÉCHECS           ")
        print("=" * 50)

    #======================== Main menu =============================
    def display_menu(self):
        """ Menu principal du programme """

        print("1. Gestion des Joueurs")
        print("2. Gestion des Tournois")
        print("3. Gestion des Rondes")
        print("4. Rapports")
        print("5. Quitter")

    def get_user_choice(self):
        choice = input("Veuillez choisir l'une des options ci-dessus")

        valid_choice = ["1", "2", "3", "4", "5"]
        if choice not in valid_choice:
            raise ValueError("Votre entrée n'est pas valide. Merci de rentrer un choix entre 1 et 4.")

        return choice

    def handle_choice(self, choice):
        if choice == "1":
            self.manage_players()
        elif choice == "2":
            self.manage_tournaments()
        elif choice == "3":
            self.manage_rounds()
        elif choice == "4":
            self.manage_reports()
        elif choice == "5":
            print("Merci d'avoir utilisé le système de tournoi d'échecs. Au revoir!")
            exit()

    def display_message(self, message):
        print(message)

    # ======================== Submenu ===============================
    def display_submenu(self, entity_name):
        """ Sous-menu de gestion des joueurs et tournois"""

        print(f"=== Gestion des {entity_name} ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Charger")
        print("4. Sauvegarder")
        print("5. Retour au menu principal")

    def display_reports_menu(self):
        """ Menu spécialisé pour les rapports"""
        
        print("=== Gestion des Rapports ===")
        print("1. Joueurs d'un tournoi")
        print("2. Tous les joueurs (alphabétique)")
        print("3. Tous les tournois")
        print("4. Informations d'un tournoi")
        print("5. Rondes et matchs d'un tournoi")
        print("6. Retour au menu principal")

    # ======================= Get info ===============================
    def get_tournament_info(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        number_players = input("Nombre de joueurs: ")
        number_rounds = input("Nombre de rondes: ")
        description = input("Description du tournoi: ")
        return name, location, number_players, number_rounds, description
    
    def get_player_info(self):
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (YYYY-MM-DD): ")
        national_id = input("ID national: ")
        return first_name, last_name, birth_date, national_id

    # ====================== def menu action ========================
    def manage_players(self):
        while True:
            self.display_submenu("Joueurs")
            choice = input("Votre choix (1-5): ")
            
            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.display_players()  
            elif choice == "3":
                self.display_message("Charger les joueurs")
            elif choice == "4":
                self.display_message("Sauvegarder les joueurs")
            elif choice == "5":
                break
            else:
                self.display_message("Choix invalide")
            
            input("Appuyez sur Entrée pour continuer...")

    #A faire
    def manage_tournaments(self):
        while True:
            self.display_submenu("Tournois")
            choice = input("votre choix (1-5): ")

            if choice == "1":
                self.create_new_tournament()
            elif choice == "2":
                self.display_tournament()
            elif choice == "3":
                self.display_message("Charger les tounois")
            elif choice == "4":
                self.display_message("Sauvegarder les tournois")
            elif choice == "5":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")

    #A faire
    def manage_rounds(self):
        while True:
            self.display_submenu("Tournois")
            choice = input("votre choix (1-5): ")

            if choice == "1":
                self.create_new_tournament()
            elif choice == "2":
                self.display_tournament()
            elif choice == "3":
                self.display_message("Charger les tounois")
            elif choice == "4":
                self.display_message("Sauvegarder les tournois")
            elif choice == "5":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")

    #A faire
    def manage_reports(self):
        while True:
            self.display_reports_menu()
            choice = input("votre choix (1-6): ")

            if choice == "1":
                self.tournament_players_report()
            elif choice == "2":
                self.display_alphabetical_players_report()
            elif choice == "3":
                self.tournaments_report()
            elif choice == "4":
                self.tournaments_info_report()
            elif choice == "5":
                self.Rounds_and_matches_report()
            elif choice == "6":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")
        pass


    # ===================== def submenu player =======================
    def create_player(self):
        self.display_message("=== Création d'un nouveau joueur ===")
        
        first_name, last_name, birth_date, national_id = self.get_player_info()
                
        if self.controller:
            success, message = self.controller.create_player_simple(first_name, last_name, birth_date, national_id)
            self.display_message(message)
        else:
            self.display_message("Controller non disponible")

    def display_players(self):
        self.display_message("=== Liste des joueurs ===")
        
        if self.controller and self.controller.players:
            for i in range(len(self.controller.players)):
                player = self.controller.players[i]
                print(f"{i+1}. {player.first_name} {player.last_name}")
                print(f"Né le: {player.date_of_birth} (âge: {player.age})")
                print(f"ID: {player.identification}")
                print()
        else:
            self.display_message("Aucun joueur créé pour le moment.")

    # ===================== def submenu tournament =======================
    def create_new_tournament(self):
        self.display_message("=== Création d'un nouveau tournoi ===")

        name, location, number_players, number_rounds, description = self.get_tournament_info()
        if self.controller:
            success, message = self.controller.create_tournament(name, location, number_players, number_rounds, description)
            self.display_message(message)
        else:
            self.display_message("Controller non disponible")
    
    def display_tournament(self):
        self.display_message("=== Liste des tournois ===")

        if self.controller and self.controller.tournaments:
            for i in range(len(self.controller.tournaments)):
                tournament=self.controller.tournaments[i]
                print(f"{i+1}. {tournament.name}")
                print(f"Se déroulera à {tournament.location}")
                print(f"Le tournoi enregistre {tournament.number_players} joueurs, qui s'affronterons sur {tournament.number_rounds} rondes.")
                print(f"{tournament.description}")
        else:
            self.display_message("Aucun tournoi de crée pour le moment")

    #======================= reports submenu ==============================
    def tournament_players_report(self):
        """Rapport sur un tournoi selectionné"""
        self.display_message("=== Sélection du tournoi ===")
        tournaments_available = []
        if self.controller.tournaments:
            for i in range(len(self.controller.tournaments)):
                tournament = self.controller.tournaments[i]
                tournaments_available.append(tournament)
                print(f"{i+1}. {tournament.name}") 
        else:
            self.display_message("Aucun tournoi de crée pour le moment")

    

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

    # ======================= Get info ===============================
    def get_tournament_info(self):
        name = input("Nom du tournoi: ")
        lieu = input("Lieu du tournoi: ")
        nb_players = input("Nombre de joueurs: ")
        nb_rounds = input("Nombre de rondes: ")
        description = input("Description du tournoi: ")
        return name, lieu, nb_players, nb_rounds, description
    
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
                self.create.tournament()
            elif choice == "2":
                self.dispay_tournament()
            elif choice == "3":
                self.display_message("Charger les tounois")
            elif choice == "4":
                self.display_message("Sauvegarder les tournoi")
            elif choice == "5":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")

    #A faire
    def manage_rounds(self):
        self.display_message("Gestion des rondes")
        input("Appuyez sur Entrée pour continuer...")

    #A faire
    def manage_reports(self):
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

        name, lieu, nb_players, nb_rounds, description = self.get_tournament_info()
        if self.controller:
            success, message = self.controller.create_tournament(name, lieu, nb_players, nb_rounds, description)
        else:
            self.display_message("Controller non disponible")
    
    def display_tournament(self):
        self.display_message("=== Liste des tournois ===")

        
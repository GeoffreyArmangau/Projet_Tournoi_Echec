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
        choice = input("Veuillez choisir l'une des options ci-dessus: ")
        
        # Nettoyer l'input en gardant seulement le premier caractère s'il est un chiffre
        choice = choice.strip()
        if choice and choice[0].isdigit():
            choice = choice[0]

        valid_choice = ["1", "2", "3", "4", "5"]
        if choice not in valid_choice:
            raise ValueError("Votre entrée n'est pas valide. Merci de rentrer un choix entre 1 et 5.")

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

    def display_rounds_menu(self):
        """Menu spécialisé pour la gestion des rondes"""
        print("=== Gestion des Rondes ===")
        print("1. Démarrer la première ronde")
        print("2. Voir les matchs en cours")
        print("3. Saisir les résultats")
        print("4. Passer à la ronde suivante")
        print("5. Voir le classement")
        print("6. Voir toutes les rondes")
        print("7. Retour au menu principal")

    def display_tournaments_menu(self):
        """Menu spécialisé pour la gestion des tournois"""
        print("=== Gestion des Tournois ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Inscrire des joueurs")
        print("4. Charger")
        print("5. Sauvegarder")
        print("6. Retour au menu principal")

    # ======================= Get info ===============================
    def get_tournament_info(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        beginning_date = input("Date de début (DD/MM/YYYY): ")
        end_date = input("Date de fin (DD/MM/YYYY): ")
        number_of_rounds = input("Nombre de rondes: ")
        description = input("Description du tournoi: ")
        return name, location, beginning_date, end_date, number_of_rounds, description
    
    def get_player_info(self):
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance (DD/MM/YYYY): ")
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
            self.display_tournaments_menu()
            choice = input("votre choix (1-6): ")

            if choice == "1":
                self.create_new_tournament()
            elif choice == "2":
                self.display_tournament()
            elif choice == "3":
                self.register_players_to_tournament()
            elif choice == "4":
                self.display_message("Charger les tournois")
            elif choice == "5":
                self.display_message("Sauvegarder les tournois")
            elif choice == "6":
                break
            else:
                self.display_message("Choix invalide")

            input("Appuyez sur Entrée pour continuer...")

    def manage_rounds(self):
        """Gestion des rondes d'un tournoi"""
        while True:
            self.display_rounds_menu()
            choice = input("Votre choix (1-7): ")

            if choice == "1":
                self.start_first_round()
            elif choice == "2":
                self.display_current_matches()
            elif choice == "3":
                self.enter_match_results()
            elif choice == "4":
                self.start_next_round()
            elif choice == "5":
                self.display_tournament_ranking()
            elif choice == "6":
                self.display_all_rounds()
            elif choice == "7":
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

        name, location, beginning_date, end_date, number_of_rounds, description = self.get_tournament_info()
        if self.controller:
            tournament = self.controller.create_tournament(name, location, beginning_date, end_date, int(number_of_rounds), description)
            self.controller.tournaments.append(tournament)
            self.display_message(f"Tournoi '{name}' créé avec succès !")
        else:
            self.display_message("Controller non disponible")
    
    def display_tournament(self):
        self.display_message("=== Liste des tournois ===")

        if self.controller and self.controller.tournaments:
            for i in range(len(self.controller.tournaments)):
                tournament=self.controller.tournaments[i]
                print(f"{i+1}. {tournament.name}")
                print(f"Se déroulera à {tournament.location}")
                print(f"Le tournoi enregistre {len(tournament.players)} joueurs, qui s'affronterons sur {tournament.max_rounds} rondes.")
                print(f"{tournament.description}")
        else:
            self.display_message("Aucun tournoi de crée pour le moment")

    def register_players_to_tournament(self):
        """Inscrire des joueurs à un tournoi"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        if not self.controller.players:
            self.display_message("Aucun joueur créé")
            return
        
        # Sélection du tournoi
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name} ({len(tournament.players)} joueurs inscrits)")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        # Sélection des joueurs
        print("\n=== Joueurs disponibles ===")
        for i in range(len(self.controller.players)):
            player = self.controller.players[i]
            print(f"{i+1}. {player.first_name} {player.last_name} ({player.identification})")
        
        player_choice = input("Choisissez le numéro du joueur à inscrire: ")
        player_index = int(player_choice) - 1
        selected_player = self.controller.players[player_index]
        
        # Ajouter le joueur au tournoi via le controller
        self.controller.add_player_to_tournament(selected_tournament, selected_player)
        self.display_message(f"Joueur {selected_player.first_name} {selected_player.last_name} inscrit au tournoi {selected_tournament.name}")

    # ===================== def submenu tournament =======================
    def start_first_round(self):
        """Démarrer la première ronde d'un tournoi"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name}")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        if selected_tournament.current_round > 0:
            self.display_message("Ce tournoi a déjà commencé")
            return
        
        self.controller.create_first_round(selected_tournament)
        self.display_message(f"Première ronde créée pour {selected_tournament.name}")

    def display_current_matches(self):
        """Voir les matchs de la ronde en cours"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name}")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        if selected_tournament.current_round == 0:
            self.display_message("Ce tournoi n'a pas encore commencé")
            return
        
        # Afficher les matchs de la ronde actuelle
        self.display_message("Fonction à compléter : afficher les matchs")

    def enter_match_results(self):
        """Saisir les résultats des matchs"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name}")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        if selected_tournament.current_round == 0:
            self.display_message("Ce tournoi n'a pas encore commencé")
            return
        
        # Saisir les résultats
        self.display_message("Fonction à compléter : saisir les résultats")

    def start_next_round(self):
        """Passer à la ronde suivante"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name}")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        if selected_tournament.current_round == 0:
            self.display_message("Ce tournoi n'a pas encore commencé")
            return
        
        # Passer à la ronde suivante
        self.display_message("Fonction à compléter : ronde suivante")

    def display_tournament_ranking(self):
        """Voir le classement du tournoi"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name}")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        if selected_tournament.current_round == 0:
            self.display_message("Ce tournoi n'a pas encore commencé")
            return
        
        # Afficher le classement
        self.display_message("Fonction à compléter : classement")

    def display_all_rounds(self):
        """Voir toutes les rondes du tournoi"""
        if not self.controller.tournaments:
            self.display_message("Aucun tournoi créé")
            return
        
        print("=== Sélection du tournoi ===")
        for i in range(len(self.controller.tournaments)):
            tournament = self.controller.tournaments[i]
            print(f"{i+1}. {tournament.name}")
        
        choice = input("Choisissez le numéro du tournoi: ")
        tournament_index = int(choice) - 1
        selected_tournament = self.controller.tournaments[tournament_index]
        
        if selected_tournament.current_round == 0:
            self.display_message("Ce tournoi n'a pas encore commencé")
            return
        
        # Afficher toutes les rondes
        self.display_message("Fonction à compléter : toutes les rondes")


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
                      
            choice = input("Choisissez le numéro d'un tournoir parmis les tournois suivant") 
            tournament_index = int(choice)-1
            selected_tournament = tournaments_available[tournament_index]

            # Récupérer et afficher le rapport des joueurs
            report_data = self.controller.get_tournament_player_report(selected_tournament)
            print("=== Joueurs du tournoi ===")
            for player_info in report_data:
                print(f"- {player_info['Prénom']} {player_info['Nom']} (ID: {player_info['Numéro ID joueur']})")

        else:
            self.display_message("Aucun tournoi de crée pour le moment")

    def display_alphabetical_players_report(self):
        """Rapport sur les joueurs par ordre alphabétique"""
        report_data = self.controller.get_all_players_alphabetical()
        
        if report_data:
            print("=== Tous les joueurs (ordre alphabétique) ===")
            for player_info in report_data:
                print(f"- {player_info['Prénom']} {player_info['Nom']} (ID: {player_info['Numéro ID joueur']})")
        else:
            self.display_message("Aucun joueur d'enregistré pour le moment")
    
    def tournaments_report(self):
        """Rapport sur tous les tournois"""
        report_data = self.controller.get_all_tournaments()
        
        if report_data:
            print("=== Tous les tournois ===")
            for tournament_info in report_data:
                print(
                    f"- {tournament_info['Nom']} à {tournament_info['Lieu']}." 
                    f" Il se déroulera du {tournament_info['Date de début']} au {tournament_info['Date de fin']} sur {tournament_info['Nombre de tours max']} rondes."
                )
                if tournament_info['Description']:
                    print(f"  Description: {tournament_info['Description']}")
                else:
                    print("  Aucune description")
        else:
            self.display_message("Aucun tournoi d'enregistré pour le moment")

    def tournaments_info_report(self):
        """Informations détaillées d'un tournoi sélectionné"""
        self.display_message("=== Sélection du tournoi ===")
        tournaments_available = []
        
        if self.controller.tournaments:
            for i in range(len(self.controller.tournaments)):
                tournament = self.controller.tournaments[i]
                tournaments_available.append(tournament)
                print(f"{i+1}. {tournament.name}")
                      
            choice = input("Choisissez le numéro d'un tournoi: ") 
            tournament_index = int(choice) - 1
            selected_tournament = tournaments_available[tournament_index]

            # Récupérer et afficher les informations du tournoi
            tournament_info = self.controller.get_tournament_info(selected_tournament)
            print(f"=== Informations du tournoi '{selected_tournament.name}' ===")
            print(f"Nom: {tournament_info['Nom']}")
            print(f"Date de début: {tournament_info['Date de début']}")
            print(f"Date de fin: {tournament_info['Date de fin']}")

        else:
            self.display_message("Aucun tournoi de créé pour le moment")



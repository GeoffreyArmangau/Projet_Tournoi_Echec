class ReportsViews:
    def __init__(self):
        pass

    def display_reports_menu(self):
        """ Menu spécialisé pour les rapports"""
        print("=== Gestion des Rapports ===")
        print("1. Joueurs d'un tournoi")
        print("2. Tous les joueurs (alphabétique)")
        print("3. Tous les tournois")
        print("4. Informations d'un tournoi")
        print("5. Rondes et matchs d'un tournoi")
        print("6. Retour au menu principal")

    def tournaments_report(self):
        """Rapport sur tous les tournois"""
        report_data = self.reports_controller.get_all_tournaments()

        if report_data:
            print("=== Tous les tournois ===")
            for tournament_info in report_data:
                print(
                    f"""- {
                        tournament_info['Nom']} à {
                        tournament_info['Lieu']}." f" Il se déroulera du {
                        tournament_info['Date de début']} au {
                        tournament_info['Date de fin']} sur {
                        tournament_info['Nombre de tours max']} rondes.""")
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

        if self.tournaments_controller.tournaments:
            for i in range(len(self.tournaments_controller.tournaments)):
                tournament = self.tournaments_controller.tournaments[i]
                tournaments_available.append(tournament)
                print(f"{i + 1}. {tournament.name}")

            choice = input("Choisissez le numéro d'un tournoi: ")
            tournament_index = int(choice) - 1
            selected_tournament = tournaments_available[tournament_index]

            # Récupérer et afficher les informations du tournoi
            tournament_info = self.reports_controller.get_tournament_info(
                selected_tournament)
            print(
                f"""=== Informations du tournoi '{
                    selected_tournament.name}' ===")
            print(f"Nom: {tournament_info['Nom']}")
            print(f"Date de début: {tournament_info['Date de début']}")
            print(f"Date de fin: {tournament_info['Date de fin']}""")

        else:
            self.display_message("Aucun tournoi de créé pour le moment")

    def rounds_and_matches_report(self):
        """Rapport sur les rondes et matchs d'un tournoi"""
        self.display_message("=== Sélection du tournoi ===")
        tournaments_available = []

        if self.tournaments_controller.tournaments:
            for i in range(len(self.tournaments_controller.tournaments)):
                tournament = self.tournaments_controller.tournaments[i]
                tournaments_available.append(tournament)
                print(f"{i + 1}. {tournament.name}")

            choice = input("Choisissez le numéro d'un tournoi: ")
            tournament_index = int(choice) - 1
            selected_tournament = tournaments_available[tournament_index]

            # Récupérer et afficher les rondes et matchs
            rounds_data = self.reports_controller.get_tournament_rounds_and_matches(
                selected_tournament)
            if rounds_data:
                for round_info in rounds_data:
                    print(f"\n=== {round_info['Ronde']} ===")
                    for i, match in enumerate(round_info['matches']):
                        j1 = match['Joueur 1']
                        j2 = match['Joueur 2']
                        j1_name = f"{j1.first_name} {j1.last_name}"
                        j2_name = f"{j2.first_name} {j2.last_name}"
                        s1, s2 = match['Score joueur 1'], match['Score joueur 2']
                        print(f"  Match {i}: {j1_name} VS {j2_name} ({s1} - {s2})")
            else:
                self.display_message("Aucune ronde disponible pour ce tournoi")
        else:
            self.display_message("Aucun tournoi de créé pour le moment")

    def display_message(self, message):
        print(message)

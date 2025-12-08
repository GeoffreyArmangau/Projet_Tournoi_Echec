class ReportsController:
    def __init__(self):
        """Initialise le contrôleur des rapports"""
        pass

    def get_tournament_player_report(self, tournament):
        """Rapport sur les joueurs du tournoi"""
        player_list = list(tournament.players)
        player_list.sort(key=lambda p: (p.last_name, p.first_name))

        player_reports = []

        for player in player_list:
            player_dict = {
                "Nom": player.last_name,
                "Prénom": player.first_name,
                "Date de naissance": player.date_of_birth,
                "Numéro ID joueur": player.identification,
            }
            player_reports.append(player_dict)

        return player_reports

    def get_all_players_alphabetical(self, players_controller):
        """Liste de tous les joueurs par ordre alphabétique"""

        all_players = players_controller.load_players_from_json()
        all_players.sort(key=lambda p: (p.last_name, p.first_name))

        players_list = []
        for player in all_players:
            player_dict = {
                "Nom": player.last_name,
                "Prénom": player.first_name,
                "Date de naissance": player.date_of_birth,
                "Age": player.age,
                "Numéro ID joueur": player.identification,
            }
            players_list.append(player_dict)

        return players_list

    def get_all_tournaments(self, tournaments_controller):
        """Liste de tous les tournois"""

        # Charger tous les tournois depuis JSON
        all_tournaments = tournaments_controller.load_tournaments_from_json()

        if all_tournaments:
            all_tournaments.sort(key=lambda t: t.name)

        tournament_list = []
        for tournament in all_tournaments:
            tournament_dict = {
                "Nom": tournament.name,
                "Lieu": tournament.location,
                "Date de début": tournament.beginning_date,
                "Date de fin": tournament.end_date,
                "Nombre de tours max": tournament.max_rounds,
                "Tour actuel": tournament.actual_round,
                "Description": tournament.description
            }
            tournament_list.append(tournament_dict)

        return tournament_list

    def get_tournament_info(self, tournament):
        """Nom et dates d'un tournoi donné"""

        tournament_info = {
            "Nom": tournament.name,
            "Date de début": tournament.beginning_date,
            "Date de fin": tournament.end_date,
        }

        return tournament_info

    def get_tournament_rounds_and_matches(self, tournament):
        """Liste de tous les tours du tournoi et de tous les matchs du tour"""

        rounds_data = []

        for round_obj in tournament.rounds:
            round_dict = {
                "Ronde": round_obj.name,
                "Début": round_obj.start_datetime,
                "Fin": round_obj.end_datetime,
                "Completion": round_obj.is_completed,
                "Matchs": []
            }

            for match in round_obj.matches:
                match_dict = {
                    "Joueur 1": match.player1,
                    "Joueur 2": match.player2,
                    "Score joueur 1": match.score1,
                    "Score joueur 2": match.score2
                }
                round_dict["Matchs"].append(match_dict)

            rounds_data.append(round_dict)

        return rounds_data

    def get_tournament_ranking(self, tournament):
        """Calcule et retourne le classement actuel du tournoi"""
        if tournament.actual_round == 0:
            return []

        # Calculer les scores totaux des joueurs
        player_scores = {}
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                player_scores[match.player1] = player_scores.get(
                    match.player1, 0) + match.score1
                player_scores[match.player2] = player_scores.get(
                    match.player2, 0) + match.score2

        # Trier par score décroissant
        sorted_players = sorted(
            player_scores.items(),
            key=lambda x: x[1],
            reverse=True)

        ranking = []
        for i, (player, score) in enumerate(sorted_players, 1):
            ranking.append({
                "position": i,
                "player": player,
                "score": score
            })

        return ranking
    
    def manage_reports(self, view, tournaments_controller):
        while True:
            view.display_reports_menu()
            choice = input("votre choix (1-6): ")
            if choice == "1":
                self.tournament_players_report(view, tournaments_controller)
            elif choice == "2":
                self.display_alphabetical_players_report(view)
            elif choice == "3":
                self.tournaments_report(view, tournaments_controller)
            elif choice == "4":
                self.tournaments_info_report(view, tournaments_controller)
            elif choice == "5":
                self.rounds_and_matches_report(view, tournaments_controller)
            elif choice == "6":
                break
            else:
                view.display_message("Choix invalide")
            input("Appuyez sur Entrée pour continuer...")

    def tournament_players_report(self, view, tournaments_controller):
        view.display_message("=== Sélection du tournoi ===")
        tournaments_available = tournaments_controller.tournaments
        if tournaments_available:
            for i, tournament in enumerate(tournaments_available):
                print(f"{i + 1}. {tournament.name}")
            choice = input("Choisissez le numéro d'un tournoi parmi les tournois suivants: ")
            tournament_index = int(choice) - 1
            selected_tournament = tournaments_available[tournament_index]
            report_data = self.get_tournament_player_report(selected_tournament)
            print("=== Joueurs du tournoi ===")
            for player_info in report_data:
                print(f"- {player_info['Prénom']} {player_info['Nom']} (ID: {player_info['Numéro ID joueur']})")
        else:
            view.display_message("Aucun tournoi de créé pour le moment")

    def display_alphabetical_players_report(self, view, players_controller):
        report_data = self.get_all_players_alphabetical(players_controller)
        if report_data:
            print("=== Tous les joueurs (ordre alphabétique) ===")
            for player_info in report_data:
                print(f"- {player_info['Prénom']} {player_info['Nom']} (ID: {player_info['Numéro ID joueur']})")
        else:
            view.display_message("Aucun joueur enregistré")

    def tournaments_report(self, view, tournaments_controller):
        tournament_list = self.get_all_tournaments(tournaments_controller)
        if tournament_list:
            print("=== Liste des tournois enregistrés ===")
            for tournament in tournament_list:
                print(f"- {tournament['Nom']} | Lieu : {tournament['Lieu']} | Début : {tournament['Date de début']} | Fin : {tournament['Date de fin']} | Tours max : {tournament['Nombre de tours max']} | Tour actuel : {tournament['Tour actuel']} | Description : {tournament['Description']}")
        else:
            view.display_message("Aucun tournoi enregistré")

    def tournaments_info_report(self, view, tournaments_controller):
        tournaments_available = tournaments_controller.tournaments
        if tournaments_available:
            print("=== Sélection du tournoi ===")
            for i, tournament in enumerate(tournaments_available):
                print(f"{i + 1}. {tournament.name}")
            choice = input("Choisissez le numéro d'un tournoi parmi les tournois suivants: ")
            try:
                tournament_index = int(choice) - 1
                selected_tournament = tournaments_available[tournament_index]
            except (ValueError, IndexError):
                view.display_message("Numéro de tournoi invalide")
                return
            info = self.get_tournament_info(selected_tournament)
            print("=== Informations sur le tournoi ===")
            for key, value in info.items():
                print(f"{key} : {value}")
        else:
            view.display_message("Aucun tournoi enregistré")

    def rounds_and_matches_report(self, view, tournaments_controller):
        tournaments_available = tournaments_controller.tournaments
        if tournaments_available:
            print("=== Sélection du tournoi ===")
            for i, tournament in enumerate(tournaments_available):
                print(f"{i + 1}. {tournament.name}")
            choice = input("Choisissez le numéro d'un tournoi parmi les tournois suivants: ")

            try:
                tournament_index = int(choice) - 1
                selected_tournament = tournaments_available[tournament_index]
            except (ValueError, IndexError):
                view.display_message("Numéro de tournoi invalide")
                return
            
            print(f"=== Rounds et matchs du tournoi {selected_tournament.name} ===")
            for round_obj in selected_tournament.rounds:
                print(f"\n{round_obj.name}")
                for match in round_obj.matches:
                    player1 = f"{match.player1.first_name} {match.player1.last_name}"
                    player2 = f"{match.player2.first_name} {match.player2.last_name}"
                    print(f"  {player1} ({match.player1_color}) vs {player2} ({match.player2_color}) | Score : {match.score1} - {match.score2}")
        else:
            view.display_message("Aucun tournoi enregistré")

    

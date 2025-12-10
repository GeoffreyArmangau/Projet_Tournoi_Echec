class ReportsController:
    def __init__(self) -> None:
        """
        Initialise le contrôleur des rapports pour la génération de rapports sur les joueurs et tournois.
        """

    def get_tournament_player_report(self, tournament):
        """
        Génère un rapport détaillé sur les joueurs d'un tournoi donné.
        Retourne une liste de dictionnaires avec les informations des joueurs.
        """
        player_list = list(tournament.players)

        player_reports = []
        for player in player_list:
            player_dict = {
                "Nom": player.last_name,
                "Prénom": player.first_name,
                "Date de naissance": player.date_of_birth,
                "Numéro ID joueur": player.identification
            }
            player_reports.append(player_dict)

        return player_reports

    def get_all_players_alphabetical(self, players_controller):
        """
        Retourne la liste de tous les joueurs triés par ordre alphabétique (nom, prénom).
        """
        all_players = players_controller.load_players_from_json()
        all_players.sort(key=lambda p: (p.last_name, p.first_name))

        players_list = []
        for player in all_players:
            player_dict = {
                "Nom": player.last_name,
                "Prénom": player.first_name,
                "Date de naissance": player.date_of_birth,
                "Age": player.age,
                "Numéro ID joueur": player.identification
            }
            players_list.append(player_dict)

        return players_list

    def get_all_tournaments(self, tournaments_controller):
        """
        Retourne la liste de tous les tournois enregistrés, triés par nom.
        """
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
        """
        Retourne un dictionnaire avec le nom et les dates d'un tournoi donné.
        """
        tournament_info = {
            "Nom": tournament.name,
            "Date de début": tournament.beginning_date,
            "Date de fin": tournament.end_date
        }
        return tournament_info

    def get_tournament_rounds_and_matches(self, tournament):
        """
        Retourne la liste de tous les rounds et des matchs associés pour un tournoi donné.
        """
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
        """
        Calcule et retourne le classement actuel du tournoi sous forme de liste ordonnée.
        """
        if tournament.actual_round == 0:
            return []
        # Calculer les scores totaux des joueurs
        player_scores = {}
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                player_scores[match.player1] = player_scores.get(match.player1, 0) + match.score1
                player_scores[match.player2] = player_scores.get(match.player2, 0) + match.score2

        # Trier par score décroissant
        sorted_players = sorted(
            player_scores.items(), key=lambda x: x[1], reverse=True)

        ranking = []
        for i, (player, score) in enumerate(sorted_players, 1):
            ranking.append({
                "position": i,
                "player": player,
                "score": score
            })

        return ranking

    def manage_reports(self, view, tournaments_controller, players_controller) -> None:
        """
        Affiche le menu des rapports et gère les actions utilisateur pour la génération de rapports.
        """
        while True:
            view.display_reports_menu()
            choice: str = input("votre choix (1-6): ")
            if choice == "1":
                self.tournament_players_report(view, tournaments_controller)
            elif choice == "2":
                self.display_alphabetical_players_report(view, players_controller)
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

    def tournament_players_report(self, view, tournaments_controller) -> None:
        """
        Affiche le rapport des joueurs pour un tournoi sélectionné.
        """
        view.display_message("=== Sélection du tournoi ===")
        tournaments_available = tournaments_controller.tournaments
        if tournaments_available:
            for i, tournament in enumerate(tournaments_available):
                print(f"{i + 1}. {tournament.name}")
            choice: str = input("Choisissez le numéro d'un tournoi parmi les tournois suivants: ")
            tournament_index: int = int(choice) - 1
            selected_tournament = tournaments_available[tournament_index]
            report_data = self.get_tournament_player_report(selected_tournament)
            print("=== Joueurs du tournoi ===")
            for player_info in report_data:
                print(f"- {player_info['Prénom']} {player_info['Nom']} (ID: {player_info['Numéro ID joueur']})")
        else:
            view.display_message("Aucun tournoi de créé pour le moment")

    def display_alphabetical_players_report(self, view, players_controller) -> None:
        """
        Affiche la liste de tous les joueurs triés par ordre alphabétique.
        """
        report_data = self.get_all_players_alphabetical(players_controller)
        if report_data:
            print("=== Tous les joueurs (ordre alphabétique) ===")
            for player_info in report_data:
                print(f"- {player_info['Prénom']} {player_info['Nom']} (ID: {player_info['Numéro ID joueur']})")
        else:
            view.display_message("Aucun joueur enregistré")

    def tournaments_report(self, view, tournaments_controller) -> None:
        """
        Affiche la liste de tous les tournois enregistrés avec leurs informations principales.
        """
        tournament_list = self.get_all_tournaments(tournaments_controller)
        if tournament_list:
            print("=== Liste des tournois enregistrés ===")
            for tournament in tournament_list:
                desc = tournament['Description'][:60]
                print(f"- {tournament['Nom']} | Lieu : {tournament['Lieu']} | Début : {tournament['Date de début']} | "
                      f"Fin : {tournament['Date de fin']} | Tours max : {tournament['Nombre de tours max']} | "
                      f"Tour actuel : {tournament['Tour actuel']} | Description : {desc}")
        else:
            view.display_message("Aucun tournoi enregistré")

    def tournaments_info_report(self, view, tournaments_controller) -> None:
        """
        Affiche les informations détaillées d'un tournoi sélectionné.
        """
        tournaments_available = tournaments_controller.tournaments
        if tournaments_available:
            print("=== Sélection du tournoi ===")
            for i, tournament in enumerate(tournaments_available):
                print(f"{i + 1}. {tournament.name}")
            choice: str = input("Choisissez le numéro d'un tournoi parmi les tournois suivants: ")
            try:
                tournament_index: int = int(choice) - 1
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

    def rounds_and_matches_report(self, view, tournaments_controller) -> None:
        """
        Affiche le détail des rounds et des matchs pour un tournoi sélectionné.
        """
        tournaments_available = tournaments_controller.tournaments
        if tournaments_available:
            print("=== Sélection du tournoi ===")
            for i, tournament in enumerate(tournaments_available):
                print(f"{i + 1}. {tournament.name}")
            choice: str = input("Choisissez le numéro d'un tournoi parmi les tournois suivants: ")

            try:
                tournament_index: int = int(choice) - 1
                selected_tournament = tournaments_available[tournament_index]
            except (ValueError, IndexError):
                view.display_message("Numéro de tournoi invalide")
                return
            print(f"=== Rounds et matchs du tournoi {selected_tournament.name} ===")
            for round_obj in selected_tournament.rounds:
                print(f"\n{round_obj.name}")
                print(f"  Début : {round_obj.start_datetime}")
                print(f"  Fin   : {round_obj.end_datetime}")
                for match in round_obj.matches:
                    player1: str = f"{match.player1.first_name} {match.player1.last_name}"
                    player2: str = f"{match.player2.first_name} {match.player2.last_name}"
                    print(f"{player1} ({match.player1_color}) vs {player2} ({match.player2_color}) | "
                          f"Score : {match.score1} - {match.score2}")
        else:
            view.display_message("Aucun tournoi enregistré")

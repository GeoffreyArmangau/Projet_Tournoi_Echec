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
                player_scores[match.player1] = player_scores.get(match.player1, 0) + match.score1
                player_scores[match.player2] = player_scores.get(match.player2, 0) + match.score2
        
        # Trier par score décroissant
        sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
        
        ranking = []
        for i, (player, score) in enumerate(sorted_players, 1):
            ranking.append({
                "position": i,
                "player": player,
                "score": score
            })
        
        return ranking

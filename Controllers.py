from Models.Match import Match
from Models.Player import Player
from Models.Tournament import Tournament
from Models.Round import Round
import json
import random
from datetime import datetime

class Controllers:
    def __init__(self):
        """Initialise les listes pour stocker les données"""
        self.players = []
        self.tournaments = []
        self.rounds = []

    #===========================player controller===========================#
    def create_player_simple(self, first_name, last_name, birth_date, national_id):
        """Crée un nouveau joueur avec la logique métier"""
        try:
            # Validation des champs vides
            if not all([first_name, last_name, birth_date, national_id]):
                return False, "Tous les champs sont obligatoires !"
            
            # Logique métier : calculer l'âge automatiquement
            current_year = datetime.now().year
            birth_year = int(birth_date.split('-')[0])
            age = current_year - birth_year
            
            # Créer le joueur
            player = Player(first_name, last_name, birth_date, age, national_id)
            
            # Stocker le joueur dans la liste
            self.players.append(player)
            
            return True, f"Joueur {first_name} {last_name} créé avec succès !"
            
        except Exception as e:
            return False, f"Erreur lors de la création: {e}"

    def add_player_to_tournament(self, tournament, player):
        tournament.players.append(player)
        return tournament

        #===========================tournament controller===========================#
    def create_tournament(self, name, location, beginning_date, end_date, number_of_rounds=4, description=""):
        tournament = Tournament(
            name, 
            location, 
            beginning_date, 
            end_date, 
            max_rounds=number_of_rounds, 
            description=description
        )
        return tournament
    

    #=========================Match controller===============================#
    """
    Gère le contrôleur des scores
    """
    def set_score(self, score_1, score_2):
        """
        Attribut les scores d'un match
        """
        valid_scores = [0, 0.5, 1] 

        #Vérifie que les scores entrés soient valides
        if score_1 not in valid_scores or score_2 not in valid_scores:
            raise ValueError ("Score invalide: les scores doivent être 0, 0.5 ou 1")
        
        #Vérifie que les scores de tous le match soient entrés
        if score_1 + score_2 != 1:
            raise ValueError ("le score total du match doit être de 1 pour couvrir un gagnat + un perdant ou une égalité")

        self.score_1 = score_1
        self.score_2 = score_2
    
    def get_winner(self):
        """
        Déterminer le gagnant du match ou l'égalité
        """
        if self.score_1 > self.score_2:
            return f'{self.Player_1.first_name} gagne le match contre {self.Player_2.first_name}'
        elif self.score_1 < self.score_2:
            return f'{self.Player_2.first_name} gagne le match contre {self.Player_1.first_name}'
        else:
            return f'Égalité entre {self.player_1.first_name} et {self.player_2.first_name}'
        
    def is_completed(self):
        """
        Vérfifie qu'un match soit terminé
        """
        return self.score_1 != 0 or self.score_2 != 0
    
    def match_to_dictionary(self):
        return {
            "player_1_name" : self.player1.last_name,
            "player_1_ID": self.player1.identification,
            "player_1_score": self.score1,
            "player_2_name" : self.player2.last_name,
            "player_2_ID": self.player2.identification,
            "player_2_score": self.score2
        }
    
    def __str__(self):
        """"
        Représentation textuelle du match
        """
        status()
        if self.is_completed():
            status = "En attente"
        else:
            status = f'{self.player_1.first_name}{self.score_1} : {self.player_2.first_name}{self.score_2} / Match terminé'
  
    #===========================round controller===========================#
    """
    Gérer les rondes du tournoi
    """   

    def add_match_to_round(self, round_obj, match):
        """
        Ajoute un match au round.
        """
        if round_obj.is_completed:
            raise ValueError ("Impossible d'ajouter un match à un tour terminé")
        
        round_obj.matches.append(match)
        return round_obj
       
    def create_first_round(self, tournament):
        """
        Gérer la première ronde.

        Ici les joueurs doivent s'affronter dans l'oredre 1vs2 et 3vs4 ou plus
        """
        if len(tournament.players) < 2:
            raise ValueError("Le nombre de joueurs est insuffisant pour créer un appariement.")
        
        if len(tournament.players) % 2 != 0:
            raise ValueError("Le nombre de joueurs n'est pas un nombre pair. Il est donc impossible de faire des appariements.")            

        #creer la première ronde
        first_round = Round(round_number=1)
        shuffled_players = tournament.players.copy()
        random.shuffle(shuffled_players)
        for i in range (0, len(shuffled_players), 2):
            player_1 = shuffled_players[i]
            player_2 = shuffled_players[i + 1]
            match = Match(player_1, player_2)
            self.add_match_to_round(first_round, match)
        
        #ajouter la ronde au tournoi
        tournament.rounds.append(first_round)
        tournament.actual_round += 1

        return first_round
    
    def get_played_matches(self, tournament):
        """
        Retourne les appariement déjà joués
        """
        played_matches = set()
        for round_obj in tournament.rounds:  # Parcourir toutes les rondes
            for match in round_obj.matches:  # Parcourir tous les matchs
                # Ajouter la paire (dans les deux sens pour éviter les problèmes d'ordre)
                played_matches.add((match.player1, match.player2))
                played_matches.add((match.player2, match.player1))
        return played_matches
    
    def next_round(self, tournament):
        """
        Gère les rondes à partir de la manche 2.
        """
        
        if tournament.actual_round > tournament.max_rounds:
            raise ValueError ("Le nombre de round max est atteint")

        if not tournament.rounds == []:
            last_round = tournament.rounds[-1]

            for match in last_round.matches:
                if match.score1 == 0 and match.score2 == 0:
                    raise ValueError ("les matchs de la dernière ronde ne sont pas terminés")
        
        #récupération des scores avant tri
        total_player_scores = {}
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                total_player_scores[match.player1] = total_player_scores.get(match.player1, 0) + match.score1
                total_player_scores[match.player2] = total_player_scores.get(match.player2, 0) + match.score2
        
        #tri des joueurs avant la nouvelle ronde, randomisation en cas d'égalité
        def get_score(player_score_pair):
            return (player_score_pair[1], random.random())  

        sorted_players = sorted(total_player_scores.items(), key=get_score, reverse=True)
        
        new_round = Round(round_number=1+tournament.actual_round)
        played_matches = self.get_played_matches(tournament)
        
        #récupérer la liste des joueurs classé
        available_player = []
        for player, score in sorted_players:
            available_player.append(player)

        #appariement en évitant une rencontre double
        while len(available_player) >= 2:
            player_1 = available_player[0]
            for player in available_player[1:]:
                player_2 = player
                if (player_1, player_2) not in played_matches:             
                    match = Match(player_1, player_2)
                    self.add_match_to_round(new_round, match)
                    available_player.remove(player_1)
                    available_player.remove(player_2)
                    break
            else:
                raise ValueError ("aucun match de disponible")
     
        #ajouter la ronde au tournoi
        tournament.rounds.append(new_round)
        tournament.actual_round += 1
        
        return new_round

    def get_round_result(self):
        """
        Retourne le résultats du tour sous forme de dictionnaire
        """
#===========================reports controller===========================#

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
    
    def get_all_players_alphabetical(self):
        """Liste de tous les joueurs par ordre alphabétique"""
        
        all_players = []           
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
    
    def get_all_tournaments(self):
        """Liste de tous les tournois"""
        
        # Charger tous les tournois depuis JSON
        all_tournaments = self.load_tournaments_from_json()
        
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
        
        # Étape 1 : Créer une liste pour stocker le résultat
        rounds_data = []

        for round in tournament.rounds:
            round_dict ={
                "Ronde": round.name,
                "Début": round.start_datetime,
                "Fin": round.end_datetime,
                "Completion": round.is_completed,
                "Matchs": []
            }
            
            for match in round.matches:
                match_dict = {
                    "Joueur 1": match.player1,
                    "Joueur 2": match.player2,
                    "Score joueur 1": match.score1,
                    "Score joueur 2": match.score2
                }
                round_dict["Matchs"].append(match_dict)

            rounds_data.append(round_dict)
        
        # Étape 2 : Pour l'instant, on retourne la liste vide
        return rounds_data

    #===========================JSON controller===========================#
    
    def save_player_to_json(self, player):
        """Sauvegarde un joueur dans players.json"""
        try:
            with open('players.json', 'r') as file:
                players = json.load(file)
        except FileNotFoundError:
            players = []
        
        players.append(player.Player_Dictionary())
        
        with open('players.json', 'w') as file:
            json.dump(players, file, indent=4)
    
    def load_players_from_json(self):
        """Charge tous les joueurs depuis players.json"""
        try:
            with open('players.json', 'r') as file:
                players_data = json.load(file)
                players = []
                for player_data in players_data:
                    player = Player(
                        player_data['first_name'],
                        player_data['last_name'],
                        player_data['date_of_birth'],
                        player_data['age'],
                        player_data['identification']
                    )
                    players.append(player)
                return players
        except FileNotFoundError:
            return []
    
    def save_tournament_to_json(self, tournament):
        """Sauvegarde un tournoi dans tournaments.json"""
        try:
            with open('tournaments.json', 'r') as file:
                tournaments = json.load(file)
        except FileNotFoundError:
            tournaments = []
        
        # Version simplifiée du Tournament_Dictionary (sans rounds/players pour l'instant)
        tournament_dict = {
            "name": tournament.name,
            "location": tournament.location,
            "beginning_date": tournament.beginning_date,
            "end_date": tournament.end_date,
            "max_rounds": tournament.max_rounds,
            "actual_round": tournament.actual_round,
            "description": tournament.description,
            "players_count": len(tournament.players),
            "rounds_count": len(tournament.rounds)
        }
        
        tournaments.append(tournament_dict)
        
        with open('tournaments.json', 'w') as file:
            json.dump(tournaments, file, indent=4)
    
    def load_tournaments_from_json(self):
        """Charge tous les tournois depuis tournaments.json"""
        try:
            with open('tournaments.json', 'r') as file:
                tournaments_data = json.load(file)
                tournaments = []
                for tournament_data in tournaments_data:
                    tournament = Tournament(
                        name=tournament_data['name'],
                        location=tournament_data['location'],
                        beginning_date=tournament_data['beginning_date'],
                        end_date=tournament_data['end_date'],
                        max_rounds=tournament_data['max_rounds'],
                        actual_round=tournament_data['actual_round'],
                        description=tournament_data['description']
                    )
                    tournaments.append(tournament)
                return tournaments
        except FileNotFoundError:
            return []
    
    def save_tournament_complete_to_json(self, tournament):
        """Sauvegarde complète d'un tournoi avec rounds, matches et joueurs"""
        try:
            with open('tournaments_complete.json', 'r') as file:
                tournaments = json.load(file)
        except FileNotFoundError:
            tournaments = []
        
        # Utiliser la méthode Tournament_Dictionary complète
        tournaments.append(tournament.Tournament_Dictionary())
        
        with open('tournaments_complete.json', 'w') as file:
            json.dump(tournaments, file, indent=4)
    
    def load_tournament_complete_from_json(self, tournament_name):
        """Charge un tournoi complet depuis JSON par son nom"""
        try:
            with open('tournaments_complete.json', 'r') as file:
                tournaments_data = json.load(file)
                
            for tournament_data in tournaments_data:
                if tournament_data['name'] == tournament_name:
                    # Reconstruire les joueurs
                    players = []
                    for player_data in tournament_data['players']:
                        player = Player(
                            player_data['first_name'],
                            player_data['last_name'],
                            player_data['date_of_birth'],
                            player_data['age'],
                            player_data['identification']
                        )
                        players.append(player)
                    
                    # Créer le tournoi
                    tournament = Tournament(
                        name=tournament_data['name'],
                        location=tournament_data['location'],
                        beginning_date=tournament_data['beginning_date'],
                        end_date=tournament_data['end_date'],
                        max_rounds=tournament_data['max_rounds'],
                        actual_round=tournament_data['actual_round'],
                        rounds=[],  # On va reconstruire les rounds
                        players=players,
                        description=tournament_data['description']
                    )
                    
                    # Reconstruire les rounds et matches
                    from Models.Round import Round
                    for round_data in tournament_data['rounds']:
                        # Créer le round
                        round_obj = Round()
                        round_obj.name = round_data['name']
                        round_obj.start_datetime = round_data['start_datetime']
                        round_obj.end_datetime = round_data['end_datetime']
                        round_obj.is_started = round_data['is_started']
                        round_obj.is_completed = round_data['is_completed']
                        
                        # Reconstruire les matches
                        for match_data in round_data['matches']:
                            # Trouver les joueurs par ID
                            player1 = next((p for p in players if p.identification == match_data['player1_id']), None)
                            player2 = next((p for p in players if p.identification == match_data['player2_id']), None)
                            
                            if player1 and player2:
                                match = Match(player1, player2, match_data['score1'], match_data['score2'])
                                round_obj.matches.append(match)
                        
                        tournament.rounds.append(round_obj)
                    
                    return tournament
                    
            return None  # Tournoi non trouvé
            
        except FileNotFoundError:
            return None



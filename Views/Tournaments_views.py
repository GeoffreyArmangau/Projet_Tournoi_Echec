class TournamentsViews:
    def __init__(self):
        pass

    def display_tournaments_menu(self):
        """Menu spécialisé pour la gestion des tournois"""
        print("=== Gestion des Tournois ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Inscrire des joueurs")
        print("4. Lancer un tournoi")
        print("6. Retour au menu principal")

    def get_tournament_info(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        beginning_date = input("Date de début (DD/MM/YYYY): ")
        end_date = input("Date de fin (DD/MM/YYYY): ")
        number_of_rounds = input("Nombre de rondes: ")
        description = input("Description du tournoi: ")
        return name, location, beginning_date, end_date, number_of_rounds, description

    def display_message(self, message):
            print(message)
            
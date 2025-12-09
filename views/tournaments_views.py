class TournamentsViews:
    """
    Gère l'affichage et la saisie des informations liées aux tournois.
    """
    def __init__(self):
        """
        Initialise la vue des tournois.
        """
        pass

    def display_tournaments_menu(self):
        """
        Affiche le menu spécialisé pour la gestion des tournois.
        """
        print("=== Gestion des Tournois ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Inscrire des joueurs")
        print("4. Lancer un tournoi")
        print("6. Retour au menu principal")

    def get_tournament_info(self):
        """
        Demande à l'utilisateur de saisir les informations d'un tournoi et les retourne.
        """
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        beginning_date = input("Date de début (DD/MM/YYYY): ")
        end_date = input("Date de fin (DD/MM/YYYY): ")
        number_of_rounds = input("Nombre de rondes: ")
        description = input("Description du tournoi: ")
        return name, location, beginning_date, end_date, number_of_rounds, description

    def display_message(self, message):
        """
        Affiche un message à l'utilisateur.
        """
        print(message)

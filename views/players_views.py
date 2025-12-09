class PlayersViews:
    """
    Gère l'affichage et la saisie des informations liées aux joueurs.
    """
    def __init__(self):
        """
        Initialise la vue des joueurs.
        """
        pass

    def get_player_info(self):
        """
        Demande à l'utilisateur de saisir les informations d'un joueur et les retourne.
        """
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        date_of_birth = input("Date de naissance (DD/MM/YYYY): ")
        national_id = input("ID national: ")
        return first_name, last_name, date_of_birth, national_id

    def display_message(self, message):
        """
        Affiche un message à l'utilisateur.
        """
        print(message)

    def display_submenu(self, entity_name):
        """
        Affiche le sous-menu de gestion pour l'entité spécifiée (joueurs ou tournois).
        """
        print(f"=== Gestion des {entity_name} ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Charger")
        print("4. Sauvegarder")
        print("5. Retour au menu principal")

class PlayersViews:
    def __init__(self):
        pass

    def get_player_info(self):
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        date_of_birth = input("Date de naissance (DD/MM/YYYY): ")
        national_id = input("ID national: ")
        return first_name, last_name, date_of_birth, national_id

    # Les méthodes d'affichage et de saisie restent inchangées

    def display_message(self, message):
        print(message)

    def display_submenu(self, entity_name):
        """ Sous-menu de gestion des joueurs et tournois"""
        print(f"=== Gestion des {entity_name} ===")
        print("1. Créer")
        print("2. Afficher")
        print("3. Charger")
        print("4. Sauvegarder")
        print("5. Retour au menu principal")

"""
Contrôleur principal du système de tournoi
"""

from Views import View
from Controllers.Players_controllers import PlayersController
from Controllers.Tournaments_controllers import TournamentsController
from Controllers.Matches_controllers import MatchesController
from Controllers.Rounds_controllers import RoundsController
from Controllers.reports_controllers import ReportsController


def main():
    # Initialisation des contrôleurs spécialisés
    players_controller = PlayersController()
    tournaments_controller = TournamentsController()
    matches_controller = MatchesController()
    rounds_controller = RoundsController()
    reports_controller = ReportsController()

    try:
        players_controller.players = players_controller.load_players_from_json()
        tournaments_controller.tournaments = (
            tournaments_controller.load_tournaments_from_json())
        print("Données chargées avec succès!")
    except Exception as e:
        print(f"Aucune donnée précédente trouvée ou erreur de chargement: {e}")

    view = View(
        players_controller,
        tournaments_controller,
        matches_controller,
        rounds_controller,
        reports_controller)

    while True:
        try:
            view.display_header()
            view.display_menu()
            choice = view.get_user_choice()
            view.handle_choice(choice)
        except ValueError as e:
            print(f"Erreur : {e}")
            input("Appuyez sur Entrée pour continuer...")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            input("Appuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()

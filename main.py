"""
Contrôleur principal du système de tournoi
"""

from views import ViewsManager
from controllers.players_controllers import PlayersController
from controllers.tournaments_controllers import TournamentsController
from controllers.matches_controllers import MatchesController
from controllers.rounds_controllers import RoundsController
from controllers.reports_controllers import ReportsController


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

    views_manager = ViewsManager(
        players_controller,
        tournaments_controller,
        matches_controller,
        rounds_controller,
        reports_controller)

    while True:
        try:
            views_manager.display_header()
            views_manager.display_menu()
            choice = views_manager.get_user_choice()
            views_manager.handle_choice(choice)
        except ValueError as e:
            print(f"Erreur : {e}")
            input("Appuyez sur Entrée pour continuer...")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            input("Appuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()

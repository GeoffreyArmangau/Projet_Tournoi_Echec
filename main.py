"""
Contrôleur principal du système de tournoi
"""

from views.main_views import MainViews
from views.players_views import PlayersViews
from views.tournaments_views import TournamentsViews
from views.reports_views import ReportsViews
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


    players_views = PlayersViews()
    tournaments_views = TournamentsViews()
    reports_views = ReportsViews()
    views_manager = MainViews(
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
            if choice == "1":
                players_controller.manage_players(players_views)
            elif choice == "2":
                tournaments_controller.manage_tournaments(tournaments_views, players_controller, rounds_controller)
            elif choice == "3":
                reports_controller.manage_reports(reports_views, tournaments_controller)
            elif choice == "4":
                print("Merci d'avoir utilisé le système de tournoi d'échecs. Au revoir!")
                break
        except ValueError as e:
            print(f"Erreur : {e}")
            input("Appuyez sur Entrée pour continuer...")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            input("Appuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()

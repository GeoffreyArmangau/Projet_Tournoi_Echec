"""
Module Views - Gestion des interfaces utilisateur du système de tournoi d'échecs
"""

from .main_views import MainViews
from .players_views import PlayersViews
from .Tournaments_views import TournamentsViews
from .reports_views import ReportsViews

class ViewsManager:
    """
    Gestionnaire principal des vues - Remplace l'ancienne classe View monolithique
    """
    def __init__(self, players_controller, tournaments_controller, matches_controller, rounds_controller, reports_controller):
        """
        Initialise le gestionnaire avec les contrôleurs spécialisés et les vues spécialisées
        """
        self.players_controller = players_controller
        self.tournaments_controller = tournaments_controller
        self.matches_controller = matches_controller
        self.rounds_controller = rounds_controller
        self.reports_controller = reports_controller
        
        # Initialiser les vues spécialisées
        self.main_views = MainViews(players_controller, tournaments_controller, matches_controller, rounds_controller, reports_controller)
        self.players_views = PlayersViews(players_controller)
        self.tournaments_views = TournamentsViews(tournaments_controller, players_controller, rounds_controller)
        self.reports_views = ReportsViews(reports_controller, tournaments_controller)

    def display_header(self):
        """Afficher l'en-tête du menu"""
        return self.main_views.display_header()

    def display_menu(self):
        """Afficher le menu principal"""
        return self.main_views.display_menu()

    def get_user_choice(self):
        """Obtenir le choix de l'utilisateur"""
        return self.main_views.get_user_choice()

    def handle_choice(self, choice):
        """Gérer le choix de l'utilisateur"""
        return self.main_views.handle_choice(choice, self.players_views, self.tournaments_views, self.reports_views)

    def display_message(self, message):
        """Afficher un message"""
        return self.main_views.display_message(message)

# Alias pour compatibilité avec l'ancien code
View = ViewsManager

__all__ = ['ViewsManager', 'View', 'MainViews', 'PlayersViews', 'TournamentsViews', 'ReportsViews']
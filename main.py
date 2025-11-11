#!/usr/bin/env python3
"""
Contrôleur principal du système de tournoi
"""

from View import View
from Controllers import Controllers

def main():
    controller = Controllers()
    
    # Chargement automatique des données au démarrage
    try:
        controller.load_players_from_json()
        controller.load_tournaments_from_json()
        print("Données chargées avec succès!")
    except Exception as e:
        print(f"Aucune donnée précédente trouvée ou erreur de chargement: {e}")
    
    view = View(controller)
    
    while True:
        try:
            view.display_header()
            view.display_menu()
            choice = view.get_user_choice()
            view.handle_choice(choice)
        except ValueError as e:
            print(f"Erreur : {e}")
            input("Appuyez sur Entrée pour continuer...")
        except KeyboardInterrupt:
            print("\nAu revoir !")
            break
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
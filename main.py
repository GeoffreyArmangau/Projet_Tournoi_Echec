#!/usr/bin/env python3
"""
Contrôleur principal du système de tournoi
"""

from View import View
from Controllers import Controllers

def main():
    controller = Controllers()
    view = View(controller)
    
    while True:
        view.display_header()
        view.display_menu()
        choice = view.get_user_choice()
        view.handle_choice(choice)

if __name__ == "__main__":
    main()
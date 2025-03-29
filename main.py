#!/usr/bin/env python3
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: A fitness and nutrition tracking application that allows users to log their meals, workouts, and progress over time. 

import sys
sys.path.append('modules') # Add the modules directory to the Python path

from modules.menu import MainMenu
from modules.colour_sequence import color_text

def main():
    # Initialize the main menu
    main_menu = MainMenu()
    
    menu_choice = 0

    while True:
        # Display the main menu
        if(menu_choice == 0):
            menu_choice = main_menu.default_menu()
        elif(menu_choice == 1):
            # Display the food menu
            main_menu.food_log_menu()
            menu_choice = 0
        elif(menu_choice == 2):
            main_menu.exercise_log_menu()
            menu_choice = 0
        elif(menu_choice == 3):
            main_menu.monthly_progress_menu()
            menu_choice = 0
        elif(menu_choice == 4):
            main_menu.weekly_progress_menu()
            menu_choice = 0
        elif(menu_choice == 5):
            main_menu.food_menu()
            menu_choice = 0
        elif(menu_choice == 6):
            main_menu.exercise_menu()
            menu_choice = 0
        elif(menu_choice == 7):
            print(color_text("🎊 Thank you for using", "PURPLE"), color_text("NutriFitCLI", "YELLOW", True) + color_text(". Goodbye!", "PURPLE"))
            break
        
    


if __name__ == "__main__":
    main()
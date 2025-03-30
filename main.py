#!/usr/bin/env python3
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: A fitness and nutrition tracking application that allows users to log their meals, workouts, and progress over time. 

import sys # Importing sys module 
import os # Importing os module
sys.path.append('modules') # Add the modules directory to the Python path

# Importing relevant classes from the modules directory
from modules.menu import MainMenu
from modules.colour_sequence import color_text

def main():
    # Initialize the main menu
    main_menu = MainMenu()
    
    menu_choice = 0

    while True:
        # Display an appropriate menu based on the user's choice
        if(menu_choice == 0):
            menu_choice = main_menu.default_menu()
        elif(menu_choice == 1):
            menu_choice = main_menu.meal_log_menu()
        elif(menu_choice == 2):
            menu_choice = main_menu.exercise_log_menu()
        elif(menu_choice == 3):
            menu_choice = main_menu.daily_progress_menu()
        elif(menu_choice == 4):
            menu_choice = main_menu.weekly_progress_menu()
        elif(menu_choice == 5):
            menu_choice = main_menu.monthly_progress_menu()
        elif(menu_choice == 6):
            menu_choice = main_menu.yearly_progress_menu()
        elif(menu_choice == 7):
            # Exit the program
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print("")
            print("")
            print("")
            print(color_text("| 🎊 | Thank you for using", "BRIGHT_PURPLE"), color_text("NutriFitCLI", "BRIGHT_YELLOW", True) + color_text(". Goodbye! | 🎊 |", "BRIGHT_PURPLE"))
            print("")
            print("")
            print("")
            break


if __name__ == "__main__":
    main()
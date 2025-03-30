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
    # Initialize the main menu object
    main_menu = MainMenu()    
    menu_choice = 0

    # Main menu loop to keep the program running until the user exits
    while True:
        # Display an appropriate menu based on the user's choice
        match menu_choice:
            case 0:
                menu_choice = main_menu.default_menu()
            case 1:
                menu_choice = main_menu.meal_log_menu()
            case 2:
                menu_choice = main_menu.exercise_log_menu()
            case 3:
                menu_choice = main_menu.search_by_date()
            case 4:
                menu_choice = main_menu.monthly_activity_calendar()
            case 5:
                menu_choice = main_menu.total_calories_burned()
            case 6:
                # Display the exit message
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                print("")
                print("")
                print("")
                print(color_text("| 🎊 | Thank you for using", "BRIGHT_PURPLE", True), color_text("NutriFitCLI", "BRIGHT_YELLOW", True) + color_text(". Goodbye! | 🎊 |", "BRIGHT_PURPLE", True))
                print("")
                print("")
                print("")
                break # Exit the loop

if __name__ == "__main__":
    main()
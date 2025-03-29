#!/usr/bin/env python3
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: A fitness and nutrition tracking application that allows users to log their meals, workouts, and progress over time. 

import sys
sys.path.append('modules') # Add the modules directory to the Python path

from modules.menu import MainMenu

def main():
    # Initialize the main menu
    main_menu = MainMenu()

    # Display the main menu
    main_menu.display()
    
    

if __name__ == "__main__":
    main()
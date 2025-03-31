#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all menu UI logic & rendering

import os
from colour_sequence import color_text
from modules.meal_tracker import MealTracker
from modules.exercise_tracker import ExerciseTracker
from modules.data_query import QueryData

class MainMenu:
  def __init__(self):
    self.title = "NutriFitCLI"
    self.border_text = "|✨|===========================|✨|"
    self.border_text_2 = "-----------------------------------"
    
  def display_header(self, emoji="   ", menu_text="", header_color="PURPLE", space_before_emoji="           "):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    header_text = "        " + self.title + "        "  
    
    # Display app title
    print(color_text(self.border_text,  "DARK_" + header_color, True))
    print("    " + color_text(header_text,"BG_" + header_color, True, False))
    print(color_text(self.border_text,  "DARK_" + header_color, True))
    
    # Display menu title
    print(space_before_emoji + emoji + color_text(menu_text.upper() + " MENU:", "BRIGHT_" + header_color, True, True))
    
    # Top menu border
    print(color_text(self.border_text_2, "DARK_" + header_color, True))
    
  def exit_to_main_menu(self, menu_selection, exit_index=3):
    # Handle return to main menu or exit the program
    if(menu_selection == exit_index):
      return 0;    
    return 7
        
  def get_menu_input(self, menu_items, menu_colour="YELLOW"):
    # Apply color to each menu item and display it with edge borders
    for index, item in enumerate(menu_items):
      line_edge_border = color_text("|", "DARK_" + menu_colour, True)      
      print(line_edge_border + color_text(f"   {index + 1}. {item}", "BRIGHT_" + menu_colour, True) + "  " + line_edge_border)
    
    # Bottom menu border,
    print(color_text(self.border_text_2, "DARK_" + menu_colour, True))   
       
    while True:
      # Prompt user for menu input
      menu_input = input("Type the" + color_text(" menu # ", "BRIGHT_" + menu_colour, True) + "followed by " + color_text("enter key", "BRIGHT_" + menu_colour, True) + ": ")
      try:
        # If input matches number in menu, return the number
        if(int(menu_input) in range(1, menu_items.__len__() + 1)):
          user_number = int(menu_input)
          return(user_number)
        else:
          print("")
          # If the input is not in the range, display an error message
          print(color_text("Please enter a number between 1 and " + str(menu_items.__len__()) + "!", "BRIGHT_RED", True)) 
          print("")
      except ValueError:
          # If the input is not a number, display an error message
          print(color_text("Invalid input. Please enter a number.", "DARK_RED", True))
    
  # Display the main menu
  def default_menu(self): 
    menu_color = "YELLOW"
    self.display_header("📜 ", "Main", menu_color) 
    menu_items = ["Log Meal(s)              ", "Log Exercise(s)          ", "Search Logs by Date      ", "Total Calories Burned    ",  "Monthly Activity Calendar", "Exit                     "]
    return self.get_menu_input(menu_items, menu_color)    
            
  # Display the food log menu
  def meal_log_menu(self):
    # Display the food log menu
    menu_color = "CYAN"
    self.display_header("🍜 ", "Calorie", menu_color, "        ") 
    menu_items = ["Add Meal             ", "Remove Meal            ", "Main Menu           "]
    menu_selection = self.get_menu_input(menu_items, menu_color)  
    
    # Handle menu selection
    if(menu_selection == 1):   
      return MealTracker().log_meal()
    elif(menu_selection == 2):
      return MealTracker().remove_meal()   
    else:
      return self.exit_to_main_menu(menu_selection)
    
  def exercise_log_menu(self):
    # Display the exercise log menu
    menu_color = "ORANGE"
    self.display_header("👟 ", "Exercise", menu_color, "        ") 
    
    menu_items = ["Add Exercise             ", "Remove Exercise            ", "Main Menu           "]
    menu_selection = self.get_menu_input(menu_items, menu_color)  
    
    # Handle menu selection
    if(menu_selection == 1):
      return ExerciseTracker().log_exercise()
    elif(menu_selection == 2):
      return ExerciseTracker().remove_exercise()  
    else:
      return self.exit_to_main_menu(menu_selection)
    
  def search_by_date(self):
    # Display the search by date menu
    menu_color = "PURPLE"
    self.display_header("🔍 ", "Search", menu_color, "        ")     
    menu_items = ["Meals Logged By Date      ", "Workouts Logged By Date   ", "Meals & Workouts By Date  ", "Main Menu                 "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    # Handle menu selection
    if(menu_selection == 1):        
      while True:
        # Get the selected date
        target_year, target_month, target_day, exit_flag = QueryData().get_date()  
        
        # Return to main menu
        if(exit_flag):
          return 0
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"LIST OF MEALS LOGGED ON: {color_text(f"{target_year}-{target_month}-{target_day}", 'BRIGHT_YELLOW', True)}")
        # Display the calorie log for the selected date
        QueryData().meals_by_date(target_year, target_month, target_day) 
        
        user_input = input(f"Press {color_text('any key', 'BRIGHT_YELLOW', True)} to search another day" + " ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
        if(user_input == 'menu'):
          return 0 
    elif(menu_selection == 2):   
      while True:    
        # Get the selected date
        target_year, target_month, target_day, exit_flag = QueryData().get_date()  
        
        # Return to main menu
        if(exit_flag):
          return 0
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"LIST OF WORKOUTS LOGGED ON: {color_text(f"{target_year}-{target_month}-{target_day}", 'BRIGHT_YELLOW', True)}")
        # Display the calorie log for the selected date
        QueryData().exercises_by_date(target_year, target_month, target_day) 
        
        user_input = input(f"Press {color_text('any key', 'BRIGHT_YELLOW', True)} to search another day" + " ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
        if(user_input == 'menu'):
          return 0 
    elif(menu_selection == 3): 
      while True:    
        # Get the selected date
        target_year, target_month, target_day, exit_flag = QueryData().get_date()  
        
        # Return to main menu
        if(exit_flag):
          return 0
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"LIST OF MEALS LOGGED ON: {color_text(f"{target_year}-{target_month}-{target_day}", 'BRIGHT_YELLOW', True)}")
        # Display the calorie log for the selected date
        QueryData().meals_by_date(target_year, target_month, target_day)
        print(f"LIST OF WORKOUTS LOGGED ON: {color_text(f"{target_year}-{target_month}-{target_day}", 'BRIGHT_YELLOW', True)}")
        # Display the calorie log for the selected date
        QueryData().exercises_by_date(target_year, target_month, target_day) 
        
        user_input = input(f"Press {color_text('any key', 'BRIGHT_YELLOW', True)} to search another day" + " ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
        if(user_input == 'menu'):
          return 0 
    else:
      return self.exit_to_main_menu(menu_selection, 4)
             
  def total_calories_burned(self):
    # Display the total calories burned menu
    menu_color = "ORANGE"
    self.display_header("🔥 ", "Calories Burned", menu_color, "        ")     
    menu_items = ["Calories Burned By Date  ", "Calories Burned By Month ", "Main Menu                "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    # Handle menu selection
    if(menu_selection == 1):        
      while True:
        # Get the selected date
        target_year, target_month, target_day, exit_flag = QueryData().get_date()  
        
        # Return to main menu
        if(exit_flag):
          return 0
        
        # Display the calorie log for the selected date
        QueryData().calories_burned_by_date(target_year, target_month, target_day) 

        print("")
        user_input = input(f"Press {color_text('any key', 'BRIGHT_YELLOW', True)} to search another day" + " ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
        if(user_input == 'menu'):
          return 0 
    elif(menu_selection == 2):   
      while True:    
        # Get the selected date
        target_year, target_month, target_day, exit_flag = QueryData().get_date()  
        
        # Return to main menu
        if(exit_flag):
          return 0
        
        # Display the calorie log for the selected date
        QueryData().calories_burned_by_month(target_year, target_month) 
        
        print("")
        user_input = input(f"Press {color_text('any key', 'BRIGHT_YELLOW', True)} to search another month" + " ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
        if(user_input == 'menu'):
          return 0 
    else:
      return self.exit_to_main_menu(menu_selection)
    
  # Display the activity calendar
  def monthly_activity_calendar(self):
    # Display the activity calendar menu
    menu_color = "CYAN"
    self.display_header("📅 ", "Activity Calendar", menu_color, "        ")    
    menu_items = ["Calorie Log            ", "Exercise Log            ", "Main Menu           "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    # Handle menu selection
    if(menu_selection == 1):
      print("Only Meals")
    elif(menu_selection == 2):
      print("Only Exercises")  
    elif(menu_selection == 3):
      print("Meals and Exercises") 
    else:
      return self.exit_to_main_menu(menu_selection)
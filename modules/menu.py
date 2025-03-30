#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all menu UI

import os
from colour_sequence import color_text
from modules.meal_tracker import MealTracker

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
    
  def exit_to_main_menu(self, menu_selection):
    # Handle return to main menu or exit the program
    if(menu_selection == 3):
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
    menu_items = ["Log Meal(s)              ", "Log Exercise             ", "Search Logs by Date      ", "Monthly Activity Calendar", "Total Calories Burned    ", "Exit                     "]
    return self.get_menu_input(menu_items, menu_color)    
            
  # Display the food log menu
  def meal_log_menu(self):
    menu_color = "CYAN"
    self.display_header("🍜 ", "Calorie", menu_color, "        ") 
    menu_items = ["Add Meal             ", "Remove Meal            ", "Main Menu           ", "Exit                    "]
    menu_selection = self.get_menu_input(menu_items, menu_color)  
    
    if(menu_selection == 1):   
      return MealTracker().log_meal()
    elif(menu_selection == 2):
      print("Remove Exercise")    
    else:
      return self.exit_to_main_menu(menu_selection)
    
  # Display the exercise log menu
  def exercise_log_menu(self):
    menu_color = "ORANGE"
    self.display_header("👟 ", "Exercise", menu_color, "        ") 
    
    menu_items = ["Add Exercise             ", "Remove Exercise            ", "Main Menu           ", "Exit                    "]
    menu_selection = self.get_menu_input(menu_items, menu_color)  
    
    if(menu_selection == 1):
      print("Add Exercise")
    elif(menu_selection == 2):
      print("Remove Exercise")    
    else:
      return self.exit_to_main_menu(menu_selection)
    
  # Display the food log menu
  def daily_progress_menu(self):
    menu_color = "GREEN"
    self.display_header("🍜 ", "Daily Progress", menu_color, "        ")    
    menu_items = ["Calorie Log            ", "Exercise Log            ", "Main Menu           ", "Exit                    "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    if(menu_selection == 1):
      print("Add Exercise")
    elif(menu_selection == 2):
      print("Remove Exercise")    
    else:
      return self.exit_to_main_menu(menu_selection)
    
  # Display the exercise log menu
  def weekly_progress_menu(self):
    menu_color = "PURPLE"
    self.display_header("👟 ", "Weekly Progress", menu_color, "        ")     
    menu_items = ["Calorie Log            ", "Exercise Log            ", "Main Menu           ", "Exit                    "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    if(menu_selection == 1):
      print("Add Exercise")
    elif(menu_selection == 2):
      print("Remove Exercise")    
    else:
      return self.exit_to_main_menu(menu_selection)
    
  def monthly_progress_menu(self):
    menu_color = "PINK"
    self.display_header("👟 ", "Monthly Progress", menu_color, "        ") 
    
    menu_items = ["Calorie Log            ", "Exercise Log            ", "Main Menu           ", "Exit                    "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    if(menu_selection == 1):
      print("Add Exercise")
    elif(menu_selection == 2):
      print("Remove Exercise")    
    else:
      return self.exit_to_main_menu(menu_selection)
    
  def yearly_progress_menu(self):
    menu_color = "TURQUOISE"
    self.display_header("👟 ", "Yearly Progress", menu_color, "        ")     
    menu_items = ["Calorie Log            ", "Exercise Log            ", "Main Menu           ", "Exit                    "]
    menu_selection = self.get_menu_input(menu_items, menu_color)    
    
    if(menu_selection == 1):
      print("Add Exercise")
    elif(menu_selection == 2):
      print("Remove Exercise")    
    else:
      return self.exit_to_main_menu(menu_selection)
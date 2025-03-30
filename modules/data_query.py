#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with querying and displaying information about meals and exercises

import json # Importing json module

# Load ANSI color codes from a JSON file
with open('data/list_of_exercises.json') as file:
    list_of_exercises = json.load(file) 

# Load ANSI color codes from a JSON file
with open('data/list_of_foods.json') as file:
    list_of_foods = json.load(file) 
  
import os # Importing os module
from datetime import datetime # Importing datetime module
from colour_sequence import color_text

class QueryData:
  def __init__(self):
    pass
  
  def meals_by_date(self, target_year, target_month, target_day):
    pass
  
  def exercises_by_date(self, target_year, target_month, target_day):
    pass
  
  
  def calories_burned_by_date(self, target_year, target_month, target_day):
    pass
  
  def calories_burned_by_month(self, target_year, target_month):
    pass
  
  def calories_burned_by_year(self, target_year, target_month):
    pass
  
  def monthly_exercise_calendar(self, target_year, target_month):
    pass
  
  def monthly_meal_calendar(self, target_year, target_month):
    pass
  
  def monthly_mixed_calendar(self, target_year, target_month):
    pass
  
  def get_date(self):
    while True:
        # Prompt the user to enter a date
        entered_date = input("Enter the " + color_text("date ", "BRIGHT_YELLOW", True) + "(" + color_text("YYYY", "BRIGHT_YELLOW", True) + "-" + color_text("MM", "BRIGHT_YELLOW", True) + "-" + color_text("DD", "BRIGHT_YELLOW", True) + ") ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")          
        if(entered_date.lower() == "menu"):
          # Return to main menu (exit_flag = True)
          return 0, 0, 0, True       
                      
        try:
            # Try to convert the entered date to a datetime object
            correct_date = datetime.strptime(entered_date, "%Y-%m-%d")
            return correct_date.year, correct_date.month, correct_date.day, False
        except ValueError:
           print("")
           # If the date is not correct, display an error message
           print(color_text("Invalid date! Please enter the date in YYYY-MM-DD format.", "BRIGHT_RED", True)) 
           print("")     
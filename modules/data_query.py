#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with querying and displaying information about meals and exercises

import json # Importing json module

# Load ANSI color codes from a JSON file
with open('data/exercise_log.json') as file:
    exercise_log = json.load(file) 

# Load ANSI color codes from a JSON file
with open('data/food_log.json') as file:
    food_log = json.load(file) 
  
import os # Importing os module
from datetime import datetime # Importing datetime module
from colour_sequence import color_text

class QueryData:
  def __init__(self):
    pass
  
  def display_list_of_meals(self, list_of_foods):
    # Display the list of foods queried
    for index, food in enumerate(list_of_foods):
      print(f"{index + 1}. {color_text(food["name"], "BRIGHT_ORANGE", True)} | Serving size: {color_text(food['serving_size'], 'BRIGHT_PURPLE', True)} | " + color_text("Calories", "BRIGHT_PINK", True) + f" per serving: {color_text(food['calories'], 'BRIGHT_PINK', True)} | " + color_text("Grams", "BRIGHT_CYAN", True) + f" per serving: {color_text(food['grams'], 'BRIGHT_CYAN', True)}", )
    
    print("")       
    
  def display_list_of_exercises(self, list_of_exercises):
    # Display the list of exercises queried
    for index, exercise in enumerate(list_of_exercises):
      print(f"{index + 1}. {color_text(exercise["name"], "BRIGHT_ORANGE", True)} | Minutes Spent: {color_text(exercise['minutes_exercised'], 'BRIGHT_PURPLE', True)} | " + color_text("Calories Burned", "BRIGHT_PINK", True) + f": {color_text(exercise['calories_burned'], 'BRIGHT_PINK', True)}", )
      
    print("")           
        
  def meals_by_date(self, target_year, target_month, target_day):   
    # Load ANSI color codes from a JSON file
    with open('data/exercise_log.json') as file:
        exercise_log = json.load(file)
        
    date = f"{target_year}-{target_month}-{target_day}"
    
    meals_logged = self.extract_data_by_date(date, exercise_log)
    
    self.display_list_of_meals(meals_logged)   
      
    return meals_logged
        
  def exercises_by_date(self, target_year, target_month, target_day):
    # Load ANSI color codes from a JSON file
    with open('data/exercise_log.json') as file:
        exercise_log = json.load(file) 
        
    date = f"{target_year}-{target_month}-{target_day}"
    
    exercises_logged = self.extract_data_by_date(date, exercise_log)
    
    self.display_list_of_exercises(exercises_logged)   
      
    return exercises_logged
  
  def extract_data_by_date(self, target_date, data_log):
    try:
        # Filter items that match the target date
        return [item for item in data_log if item.get("date") == target_date]
    except FileNotFoundError:
        print("Error: data_log.json file not found.")
    except json.JSONDecodeError:
        print("Error: data_log.json is not a valid JSON file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
  
  
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
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    
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
           
   
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with adding and removing meal logs.

import json # Importing json module

# Load ANSI color codes from a JSON file
with open('data/list_of_foods.json') as file:
    list_of_foods = json.load(file) 
  
import os # Importing os module
from data_query import QueryData
from colour_sequence import color_text

class MealTracker:
  def __init__(self):
    self.file_path = "data/food_log.json"
    
  def log_meal(self):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    
    target_year, target_month, target_day, exit_flag = QueryData().get_date()  
    
    # Return to main menu
    if(exit_flag):
      return 0
    
    # Store the meal after getting the date
    return self.store_meal(target_year, target_month, target_day)
  
  def store_meal(self, target_year, target_month, target_day):
    keep_logging_meals = True
    
    while keep_logging_meals:
        # Prompt the user to enter a food name
        print("")
        entered_food = input("Enter " + color_text("food name", "BRIGHT_YELLOW", True)  + " ~ (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")          
        if(entered_food.lower() == "menu"):
            break
        
        # Check if food exists in the list      
        nutrition_data = self.food_search(entered_food)
        
        # If the food is not found, display an error message
        if(len(nutrition_data) == 0):
            print(color_text("Meal not found! Please try again with a different name.", "BRIGHT_RED", True)) 
        else:
            # If the food is found, display a list of names and nutrition data
            for index, food in enumerate(nutrition_data):
                print(f"{index + 1}. {color_text(food["food_name"], "BRIGHT_ORANGE", True)} | " + color_text("Calories", "BRIGHT_PINK", True) + f" per serving: {color_text(food['calories_per_serving'], 'BRIGHT_PINK', True)} | " + color_text("Grams", "BRIGHT_CYAN", True) + f" per serving: {color_text(food['grams_per_serving'], 'BRIGHT_CYAN', True)}", )
                            
            # Prompt the user to select a food from the list
            print("")
            food_selected = input("Enter" + color_text(" food", "BRIGHT_YELLOW", True) + " by " + color_text("#", "BRIGHT_YELLOW", True) + " (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
                        
            if(food_selected == 'menu'):
              break
                               
            try:
              food_selected = int(food_selected)
              self.get_serving_size(nutrition_data, food_selected, target_year, target_month, target_day)             
            except ValueError:
              print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))                
    return 0
  def food_search(self, entered_food):        
    matching_foods = []
    
    for food in list_of_foods:
      # Check if the entered food name is a substring of the food name
      if entered_food.lower() in food["food_name"].lower():  
        matching_foods.append(food)
    
    return matching_foods         
  
  def get_serving_size(self, nutrition_data, food_selected, target_year, target_month, target_day):
    try:
      if(int(food_selected) in range(1, len(nutrition_data) + 1)):
        print("")
        serving_size = input(f"Please enter a {color_text('#', 'BRIGHT_YELLOW', True)} for the {color_text("serving size", "BRIGHT_YELLOW", True)}: ")
        serving_size = int(serving_size)
        
        # Calculate the calories and grams based on the serving size entered
        selected_food = nutrition_data[int(food_selected) - 1]        
        calories = serving_size * int(selected_food["calories_per_serving"])
        grams = serving_size * int(selected_food["grams_per_serving"])   
        
        # Create a dictionary to store the food data       
        food_data = {
          "date": f"{target_year}-{target_month}-{target_day}",
          "name": selected_food["food_name"],
          "calories": calories,
          "grams": grams,
          "serving_size": serving_size,
        } 
         
        self.log_food_to_json(food_data) # Log the food to a JSON file
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console         
        print(f"Food {color_text("successfully", "BRIGHT_GREEN", True)} logged: {color_text(selected_food['food_name'], 'BRIGHT_ORANGE', True)} | Serving size: {color_text(serving_size, 'BRIGHT_PURPLE', True)} | Calories: {color_text(calories, 'BRIGHT_PINK', True)} | Grams: {color_text(grams, 'BRIGHT_CYAN', True)}")        
      else:
        print(color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED", True))
    except ValueError:
      print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))
                     
  def log_food_to_json(self, food_data):     
    try:
      # Get existing data from the JSON file
      with open(self.file_path, 'r') as file:
            existing_data = json.load(file)
      
      existing_data.append(food_data) # Add the new food data
            
      # Save the updated food data to a JSON file
      with open(self.file_path, 'w') as file:
        json.dump(existing_data, file, indent=2)  
    except FileNotFoundError:
      # If the file doesn't exist, create it
      with open(self.file_path, 'w') as file:
        json.dump([food_data], file, indent=2)
    except PermissionError:
      print(f"Error: Unable to write to {self.file_path} - permission denied.")
    except Exception as e:
        print(f"Uexpected Error: Unable to write to {self.file_path} - {e}")
        
    def delete_meal(self, target_year, target_month, target_day):
      pass
           
  
  
  
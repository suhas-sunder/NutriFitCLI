#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with adding and removing meal logs

import json

# Load ANSI color codes from a JSON file
with open('data/list_of_foods.json') as file:
    list_of_foods = json.load(file) 
  
import os

from datetime import datetime
from colour_sequence import color_text

class MealTracker:
  def __init__(self):
    self.file_path = "data/food_log.json"
    pass
  
  def get_date(self):
    while True:
        entered_date = input("Enter the " + color_text("date ", "BRIGHT_YELLOW") + "(" + color_text("YYYY", "BRIGHT_YELLOW") + "-" + color_text("MM", "BRIGHT_YELLOW") + "-" + color_text("DD", "BRIGHT_YELLOW") + "): ")
        
        try:
            correct_date = datetime.strptime(entered_date, "%Y-%m-%d")
            return correct_date.year, correct_date.month, correct_date.day
        except ValueError:
           print("")
           # If the date is not correct, display an error message
           print(color_text("Invalid date! Please enter the date in YYYY-MM-DD format.", "BRIGHT_RED")) 
           print("")
           
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
        serving_size = input("Please input the serving size: ")
        # Calculate the calories and grams based on the serving size entered
        selected_food = nutrition_data[int(food_selected) - 1]
        serving_size = int(serving_size)
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
         
        self.log_food_to_json(food_data)
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console         
        print(f"Food {color_text("successfully", "BRIGHT_GREEN", true)} logged: {color_text(selected_food['food_name'], 'BRIGHT_ORANGE')} | Serving size: {color_text(serving_size, 'BRIGHT_PURPLE')} | Calories: {color_text(calories, 'BRIGHT_PINK')} | Grams: {color_text(grams, 'BRIGHT_CYAN')}")        
      else:
        print(color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED"))
    except ValueError:
      print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED"))
           
  def store_meal(self, selftarget_year, target_month, target_day):
    keep_logging_meals = True
    
    while keep_logging_meals:
        # Prompt the user to enter a food name
        print("")
        entered_food = input("Enter " + color_text("food name", "BRIGHT_YELLOW")  + " (or " + color_text("'menu'", "BRIGHT_YELLOW") + " to " + color_text("exit", "BRIGHT_YELLOW") + "): ")          
        if(entered_food.lower() == "menu"):
            break
        
        # Check if food exists in the list      
        nutrition_data = self.food_search(entered_food)
        
        # If the food is not found, display an error message
        if(len(nutrition_data) == 0):
            print(color_text("Meal not found! Please try again with a different name.", "BRIGHT_RED")) 
        else:
            # If the food is found, display a list of names and nutrition data
            for index, food in enumerate(nutrition_data):
                print(f"{index + 1}. {color_text(food["food_name"], "BRIGHT_ORANGE")} | " + color_text("Calories", "BRIGHT_PINK") + f", per serving: {color_text(food['calories_per_serving'], 'BRIGHT_PINK')} | " + color_text("Grams", "BRIGHT_CYAN") + f", per serving: {color_text(food['grams_per_serving'], 'BRIGHT_CYAN')}", )
                            
            # Prompt the user to select a food from the list
            print("")
            food_selected = input("Enter" + color_text(" food", "BRIGHT_YELLOW") + " by " + color_text("#", "BRIGHT_YELLOW") + " (or " + color_text("'menu'", "BRIGHT_YELLOW") + " to " + color_text("exit", "BRIGHT_YELLOW") + "): ")
                        
            if(food_selected == 'menu'):
              break
                               
            try:
              food_selected = int(food_selected)
              self.get_serving_size(nutrition_data, food_selected, selftarget_year, target_month, target_day)             
            except ValueError:
              print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED"))                
    return 0
  
  def log_meal(self):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    selftarget_year, target_month, target_day = self.get_date()    
    return self.store_meal(selftarget_year, target_month, target_day)
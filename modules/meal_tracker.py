#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic related to adding and removing meal logs.

import os # Importing os module
from data_query import QueryData
from colour_sequence import ColorSequence

class MealTracker:
  def __init__(self):
    self.color_text = ColorSequence().color_text
    
  def log_meal(self):
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
      entered_food = input("Enter " + self.color_text("food name", "BRIGHT_YELLOW", True)  + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")          
      if(entered_food.lower() == "menu"):
          break
        
      # Check if food exists in the list      
      nutrition_data = self.food_search(entered_food)
        
      # If the food is not found, display an error message
      if(len(nutrition_data) == 0):
          print(self.color_text("Meal not found! Please try again with a different name.", "BRIGHT_RED", True)) 
      else:
          # If the food is found, display a list of names and nutrition data
          for index, food in enumerate(nutrition_data):
              print(f"{index + 1}. {self.color_text(food["food_name"], "BRIGHT_ORANGE", True)} | " + self.color_text("Calories", "BRIGHT_PINK", True) + f" per serving: {self.color_text(food['calories_per_serving'], 'BRIGHT_PINK', True)} | " + self.color_text("Grams", "BRIGHT_CYAN", True) + f" per serving: {self.color_text(food['grams_per_serving'], 'BRIGHT_CYAN', True)}", )
                            
          # Prompt the user to select a food from the list
          print("")
          food_selected = input("Enter" + self.color_text(" food", "BRIGHT_YELLOW", True) + " by " + self.color_text("#", "BRIGHT_YELLOW", True) + " (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
                        
          if(food_selected == 'menu'):
            break
                               
          try:
            food_selected = int(food_selected)
            self.get_serving_size(nutrition_data, food_selected, target_year, target_month, target_day)             
          except ValueError:
            print(self.color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))                
    return 0
  def food_search(self, entered_food):        
    matching_foods = []
    
    list_of_foods, _ = QueryData().list_of_items()
    
    for food in list_of_foods:
      # Check if the entered food name is a substring of the food name
      if entered_food.lower() in food["food_name"].lower():  
        matching_foods.append(food)
    
    return matching_foods         
  
  def get_serving_size(self, nutrition_data, food_selected, target_year, target_month, target_day):
    try:
      if(int(food_selected) in range(1, len(nutrition_data) + 1)):
        print("")
        serving_size = input(f"Please enter a {self.color_text('#', 'BRIGHT_YELLOW', True)} for the {self.color_text("serving size", "BRIGHT_YELLOW", True)}: ")
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
         
        QueryData().log_food_to_json(food_data) # Log the food to a JSON file
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console         
        print(f"Food {self.color_text("successfully", "BRIGHT_GREEN", True)} logged: {self.color_text(selected_food['food_name'], 'BRIGHT_ORANGE', True)} | Serving size: {self.color_text(serving_size, 'BRIGHT_PURPLE', True)} | Calories: {self.color_text(calories, 'BRIGHT_PINK', True)} | Grams: {self.color_text(grams, 'BRIGHT_CYAN', True)}")        
      else:
        print(self.color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED", True))
    except ValueError:
      print(self.color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))
                        
  
    
  def remove_meal(self):
    target_year, target_month, target_day, exit_flag = QueryData().get_date()  
    
    # Return to main menu
    if(exit_flag):
      return 0
      
    while True:
      meals_logged = QueryData().meals_by_date(target_year, target_month, target_day)
      
      if(len(meals_logged) == 0):
        # Display message if no meals logged
        print(self.color_text("No meals logged for selected date!", "BRIGHT_YELLOW", True))
        print("")
        input(f"Press {self.color_text('any key', 'BRIGHT_YELLOW', True)} to return to {self.color_text("MAIN MENU...", "BRIGHT_YELLOW", True)}")
        return 0 # Return to main menu
      
      exercise_selected = input(f"Enter the {self.color_text('#', 'BRIGHT_YELLOW', True)} to {self.color_text('delete', 'BRIGHT_YELLOW', True)} the log" + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ").strip()
      
      if(exercise_selected == 'menu'):
        return 0 # Return to main menu
         
      try:
        # Prompt user to delete meal from list
        if int(exercise_selected) in range(1, len(meals_logged) + 1):          
          QueryData().delete_meal(meals_logged[int(exercise_selected) - 1])         
          user_input = input(f"Press {self.color_text('any key', 'BRIGHT_YELLOW', True)} to delete more" + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
          if(user_input == 'menu'):
            return 0          
        else:
          print(self.color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED", True))
      except ValueError:
        print(self.color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))
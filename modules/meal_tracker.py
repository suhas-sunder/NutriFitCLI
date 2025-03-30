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
        entered_date = input("Enter the date (YYYY-MM-DD): ")
        
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
      # Save the food data to a JSON file
      with open(self.file_path, 'w') as file:
        json.dump(food_data, file, indent=2)  
    except FileNotFoundError:
      # If the file doesn't exist, create it
      with open(self.file_path, 'w') as file:
        json.dump([], file, indent=2)
               
  def food_search(self, entered_food):        
    matching_foods = []
    
    for food in list_of_foods:
      if entered_food.lower() in food["food_name"].lower():  # Partial match, case-insensitive
          matching_foods.append(food)
    
    return matching_foods
  
  def get_serving_size(self, nutrition_data, food_selected, target_year, target_month, target_day):
    try:
      if(int(food_selected) in range(1, len(nutrition_data) + 1)):
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
        print(f"Food successfully logged: {selected_food['food_name']} | Serving size: {serving_size} | Calories: {calories} | Grams: {grams}")        
      else:
        print(color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED"))
    except ValueError:
      print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED"))
           
  def store_meal(self, selftarget_year, target_month, target_day):
    keep_logging_meals = True
    
    while keep_logging_meals:
        # Prompt the user to enter a food name
        entered_food = input("Enter food name: ")          
        if(entered_food.lower() == "exit"):
            break
        
        # Check if food exists in the list      
        nutrition_data = self.food_search(entered_food)
        
        # If the food is not found, display an error message
        if(len(nutrition_data) == 0):
            print(color_text("Meal not found! Please try again with a different name.", "BRIGHT_RED")) 
        else:
            # If the food is found, display a list of names and nutrition data
            for index, food in enumerate(nutrition_data):
                print(f"{index + 1}. {food["food_name"]} | Calories per serving: {food['calories_per_serving']} | Grams per serving: {food['grams_per_serving']}", )
                                
                try:
                  # Select the food by entering its number.
                  food_selected = input("Select the food by entering its number: ")
                  self.get_serving_size(nutrition_data, food_selected, selftarget_year, target_month, target_day)    
                  break                                
                 
                except ValueError:
                  print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED"))                
    return 0
  
  def log_meal(self):
    selftarget_year, target_month, target_day = self.get_date()
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    return self.store_meal(selftarget_year, target_month, target_day)
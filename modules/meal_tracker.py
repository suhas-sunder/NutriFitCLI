import os
import requests
from datetime import datetime
from colour_sequence import color_text

class MealTracker:
  def __init__(self):
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
           
  def food_search(self, entered_food): 
       
    while True:               
        try:
            food_data = entered_food
            print(food_data)
        except ValueError:
           print("")
           # If the food is not available, display an error message
           print(color_text("Food not found! Please try again with a different name.", "BRIGHT_RED")) 
           print("")
           
  def get_meal(self):
    while True:
        entered_food = input("Enter the food name: ")        
        try:
            nutrition_data = self.food_search(entered_food)
            return nutrition_data
        except ValueError:
           print("")
           # If the meal is not available, display an error message
           print(color_text("Meal not found! Please try again with a different name.", "BRIGHT_RED")) 
           print("")
  
  def log_meal(self):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    target_year, target_month, target_day = self.get_date()
    print("Date Entered:", target_year, target_month, target_day)
    self.get_meal()
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
from colour_sequence import color_text

class DataQuery:
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
  
  
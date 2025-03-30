
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with adding and removing workout logs

import json # Importing json module

# Load ANSI color codes from a JSON file
with open('data/list_of_exercises.json') as file:
    list_of_exercises = json.load(file) 
  
import os # Importing os module
from datetime import datetime
from colour_sequence import color_text

class ExerciseTracker:
  def __init__(self):
    self.file_path = "data/exercise_log.json"
    
  def log_exercise(self):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    target_year, target_month, target_day = self.get_date()    
    return self.store_workout(target_year, target_month, target_day)
  
  def store_workout(self, target_year, target_month, target_day):
    keep_logging_workouts = True
    
    while keep_logging_workouts:
        # Prompt the user to enter a food name
        print("")
        entered_workout = input("Enter " + color_text("exercise name", "BRIGHT_YELLOW", True)  + " (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")          
        if(entered_workout.lower() == "menu"):
            break
        
        # Check if exercise exists in the list      
        workout_data = self.workout_search(entered_workout)
        
        # If the exercise is not found, display an error message
        if(len(workout_data) == 0):
            print(color_text("Exercise not found! Please try again with a different name.", "BRIGHT_RED", True)) 
        else:
            # If the exercise is found, display a list of names and workout data
            for index, exercise in enumerate(workout_data):
                print(f"{index + 1}. {color_text(exercise["exercise_name"], "BRIGHT_ORANGE", True)} | " + color_text("Calories", "BRIGHT_PINK", True) + f" burned per min: {color_text(exercise['calories_burned_per_min'], 'BRIGHT_PINK', True)}", )
                            
            # Prompt the user to select a exercise from the list
            print("")
            exercise_selected = input("Enter" + color_text(" exercise", "BRIGHT_YELLOW", True) + " by " + color_text("#", "BRIGHT_YELLOW", True) + " (or " + color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
                        
            if(exercise_selected == 'menu'):
              break
                               
            try:
              exercise_selected = int(exercise_selected)
              self.get_minutes_exercised(workout_data, exercise_selected, target_year, target_month, target_day)             
            except ValueError:
              print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))                
    return 0
  
  def workout_search(self, entered_exercise):        
    matching_exercises = []
    
    for exercise in list_of_exercises:
      # Check if the entered exercise name is a substring of the exercise name
      if entered_exercise.lower() in exercise["exercise_name"].lower():  
        matching_exercises.append(exercise)
    
    return matching_exercises
  
  def get_date(self):
    while True:
        entered_date = input("Enter the " + color_text("date ", "BRIGHT_YELLOW", True) + "(" + color_text("YYYY", "BRIGHT_YELLOW", True) + "-" + color_text("MM", "BRIGHT_YELLOW", True) + "-" + color_text("DD", "BRIGHT_YELLOW", True) + "): ")
        
        try:
            correct_date = datetime.strptime(entered_date, "%Y-%m-%d")
            return correct_date.year, correct_date.month, correct_date.day
        except ValueError:
           print("")
           # If the date is not correct, display an error message
           print(color_text("Invalid date! Please enter the date in YYYY-MM-DD format.", "BRIGHT_RED", True)) 
           print("")
  
  def get_minutes_exercised(self, workout_data, exercise_selected, target_year, target_month, target_day):
    try:
      if(int(exercise_selected) in range(1, len(workout_data) + 1)):
        print("")
        minutes_exercised = input(f"Please enter a {color_text('#', 'BRIGHT_YELLOW', True)} for the {color_text('minutes spent exercising', 'BRIGHT_YELLOW', True)}: ").strip()
        minutes_exercised = int(minutes_exercised)
        # Calculate the calories and grams based on the serving size entered
        selected_exercise = workout_data[int(exercise_selected) - 1]
        calories_burned = minutes_exercised * int(selected_exercise["calories_burned_per_min"])
        
        # Create a dictionary to store the exercise data       
        exercise_data = {
          "date": f"{target_year}-{target_month}-{target_day}",
          "name": selected_exercise["exercise_name"],
          "calories_burned": calories_burned,
          "minutes_exercised": minutes_exercised,
        } 
         
        self.log_exercise_to_json(exercise_data)
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console         
        print(f"exercise {color_text("successfully", "BRIGHT_GREEN", True)} logged: {color_text(selected_exercise['exercise_name'], 'BRIGHT_ORANGE', True)} | Minutes Exercised: {color_text(minutes_exercised, 'BRIGHT_PURPLE', True)} | Calories Burned: {color_text(calories_burned, 'BRIGHT_PINK', True)}")        
      else:
        print("")
        print(color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED", True))
    except ValueError:
      print("")
      print(color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))
              
  def log_exercise_to_json(self, exercise_data):     
    try:
      # Get existing data from the JSON file
      with open(self.file_path, 'r') as file:
            existing_data = json.load(file)
      
      existing_data.append(exercise_data) # Add the new exercise data
            
      # Save the updated exercise data to a JSON file
      with open(self.file_path, 'w') as file:
        json.dump(existing_data, file, indent=2)  
    except FileNotFoundError:
      # If the file doesn't exist, create it
      with open(self.file_path, 'w') as file:
        json.dump([exercise_data], file, indent=2)
  
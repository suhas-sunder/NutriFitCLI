
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with adding and removing workout logs
  
import os # Importing os module
from colour_sequence import ColorSequence
from data_query import QueryData

class ExerciseTracker:
  def __init__(self):
    self.color_text = ColorSequence().color_text
    
  def log_exercise(self): 
    target_year, target_month, target_day, exit_flag = QueryData().get_date()  
    
    # Return to main menu
    if(exit_flag):
      return 0
    
    return self.store_workout(target_year, target_month, target_day)
  
  def store_workout(self, target_year, target_month, target_day):
    keep_logging_workouts = True
    
    while keep_logging_workouts:
        # Prompt the user to enter an exercise name
        print("")
        entered_workout = input("Enter " + self.color_text("exercise name", "BRIGHT_YELLOW", True)  + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")          
        if(entered_workout.lower() == "menu"):
            break
        
        # Check if exercise exists in the list      
        workout_data = self.workout_search(entered_workout)
        
        # If the exercise is not found, display an error message
        if(len(workout_data) == 0):
            print(self.color_text("Exercise not found! Please try again with a different name.", "BRIGHT_RED", True)) 
        else:
            # If the exercise is found, display a list of names and workout data
            for index, exercise in enumerate(workout_data):
                print(f"{index + 1}. {self.color_text(exercise["exercise_name"], "BRIGHT_ORANGE", True)} | " + self.color_text("Calories", "BRIGHT_PINK", True) + f" burned per min: {self.color_text(exercise['calories_burned_per_min'], 'BRIGHT_PINK', True)}", )
                            
            # Prompt the user to select a exercise from the list
            print("")
            exercise_selected = input("Enter" + self.color_text(" exercise", "BRIGHT_YELLOW", True) + " by " + self.color_text("#", "BRIGHT_YELLOW", True) + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
                        
            if(exercise_selected == 'menu'):
              break
                               
            try:
              exercise_selected = int(exercise_selected)
              self.get_minutes_exercised(workout_data, exercise_selected, target_year, target_month, target_day)             
            except ValueError:
              print(self.color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))                
    return 0
  
  def workout_search(self, entered_exercise):        
    matching_exercises = []
    
    _, list_of_exercises = QueryData().list_of_items()
    
    for exercise in list_of_exercises:
      # Check if the entered exercise name is a substring of the exercise name
      if entered_exercise.lower() in exercise["exercise_name"].lower():  
        matching_exercises.append(exercise)
    
    return matching_exercises
    
  def get_minutes_exercised(self, workout_data, exercise_selected, target_year, target_month, target_day):
    try:
      if(int(exercise_selected) in range(1, len(workout_data) + 1)):
        print("")
        minutes_exercised = input(f"Please enter a {self.color_text('#', 'BRIGHT_YELLOW', True)} for the {self.color_text('minutes spent exercising', 'BRIGHT_YELLOW', True)}: ").strip()
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
         
        QueryData().log_exercise_to_json(exercise_data) # Log the exercise to a JSON file
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console         
        print(f"exercise {self.color_text("successfully", "BRIGHT_GREEN", True)} logged: {self.color_text(selected_exercise['exercise_name'], 'BRIGHT_ORANGE', True)} | Minutes Exercised: {self.color_text(minutes_exercised, 'BRIGHT_PURPLE', True)} | Calories Burned: {self.color_text(calories_burned, 'BRIGHT_PINK', True)}")        
      else:
        print("")
        print(self.color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED", True))
    except ValueError:
      print("")
      print(self.color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))
              
  def remove_exercise(self):
    target_year, target_month, target_day, exit_flag = QueryData().get_date()  
    
    # Return to main menu
    if(exit_flag):
      return 0
      
    while True:
      exercises_logged = QueryData().exercises_by_date(target_year, target_month, target_day)
      
      if(len(exercises_logged) == 0):
        # Display message if no exercises logged
        print(self.color_text("No exercises logged for selected date!", "BRIGHT_YELLOW", True))
        print("")
        input(f"Press {self.color_text('any key', 'BRIGHT_YELLOW', True)} to return to {self.color_text("MAIN MENU...", "BRIGHT_YELLOW", True)}")
        return 0 # Return to main menu
      
      exercise_selected = input(f"Enter the {self.color_text('#', 'BRIGHT_YELLOW', True)} to {self.color_text('delete', 'BRIGHT_YELLOW', True)} the log" + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ").strip()
      
      if(exercise_selected == 'menu'):
        return 0 # Return to main menu
         
      try:
        if int(exercise_selected) in range(1, len(exercises_logged) + 1):          
          QueryData().delete_exercise(exercises_logged[int(exercise_selected) - 1])         
          user_input = input(f"Press {self.color_text('any key', 'BRIGHT_YELLOW', True)} to delete more" + " ~ (or " + self.color_text("'menu'", "BRIGHT_YELLOW", True) + " for " + self.color_text("MAIN MENU", "BRIGHT_YELLOW", True) + "): ")
          if(user_input == 'menu'):
            return 0          
        else:
          print(self.color_text("Invalid selection! Please enter a valid number.", "BRIGHT_RED", True))
      except ValueError:
        print(self.color_text("Invalid input! Please enter a number.", "BRIGHT_RED", True))
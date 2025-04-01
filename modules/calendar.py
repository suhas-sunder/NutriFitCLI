#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Displays calendar UI to visualize meal and exercise logs.

import os # Importing os module
# Importing relevant classes from the modules directory
from datetime import datetime, timedelta # Importing datetime module
from colour_sequence import ColorSequence
from data_query import QueryData

class Calendar:
  def __init__(self):
    self.color_text = ColorSequence().color_text
  
  def meals_by_month(self, target_year, target_month, display_calendar = True):
    # Get meal and exercise logs
    meal_dates, workout_dates = QueryData().actvity_dates_by_month(target_year, target_month)
    
    # Format meal calendar to include highlighted days
    meals_formatted = self.format_calendar(meal_dates, "BRIGHT_GREEN", target_year, target_month)
    
    # Display calendar or return formatted list
    if(display_calendar):
      os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console 
      print("")
      print(self.color_text(f"DAYS WITH MEALS LOGGED ~ {target_year}-{target_month}:", "BRIGHT_GREEN", True))   
      print("")
      # Display highlighted calendar
      self.display_calendar(meals_formatted, "GREEN") 
    else:
      return meals_formatted
  
  def workouts_by_month(self, target_year, target_month, display_calendar = True):
    # Get meal and exercise logs
    meal_dates, workout_dates = QueryData().actvity_dates_by_month(target_year, target_month)
    
    # Format exercise calendar to include highlighted days
    workouts_formatted = self.format_calendar(workout_dates, "BRIGHT_CYAN", target_year, target_month)
    
    # Display calendar or return formatted list
    if(display_calendar):
      os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
      print("")
      print(self.color_text(f"DAYS WITH WORKOUTS LOGGED ~ {target_year}-{target_month}:", "BRIGHT_CYAN", True))    
      print("")
      # Display highlighted calendar
      self.display_calendar(workouts_formatted, "CYAN")
    else:
      return workouts_formatted
  
  def activities_by_month(self, target_year, target_month):
    # Get meal and exercise logs
    meal_dates, workout_dates = QueryData().actvity_dates_by_month(target_year, target_month)
        
    # Combine meal and exercise logs into a new list using the unpack operator
    all_activities_intersecting = meal_dates & workout_dates
    
    # Format calendar to include highlighted days for intersecting days
    intersection_formatted = self.format_calendar(all_activities_intersecting, "BRIGHT_YELLOW", target_year, target_month)    
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console 
    print("")
    print(self.color_text(f"DAYS WITH MEALS AND WORKOUTS LOGGED (INTERSECTING) ~ {target_year}-{target_month}:", "BRIGHT_YELLOW", True))  
    print("")
    
    # Display highlighted calendar
    self.display_calendar(intersection_formatted, "YELLOW")
      
  def format_calendar(self, dates_to_highlight, highlight_color, target_year, target_month):    
    # Take in the list of dates to highlight and the color to apply to them
    # Create a calendar for the month
    
    # First generate a list of all the days in the month
    days_of_month = self.generate_calendar_days_of_month(target_year, target_month)
    
    # Iterate over each day in the month and replace it in the days_of_month list with proper formatting
    for i, date in enumerate(days_of_month):      
      date_obj = datetime.strptime(date, "%Y-%m-%d")  # Convert string to datetime
      
      # Check if the current date is in the list of dates to highlight
      if date in dates_to_highlight:    
        days_of_month[i] = self.color_text(date_obj.strftime("%d"), highlight_color, True)
      else:
        days_of_month[i] = self.color_text(date_obj.strftime("%d"), "BRIGHT_WHITE", True)
        
    return days_of_month
    
  def generate_calendar_days_of_month(self, target_year, target_month):
    # Get the first day of the month
    first_day = datetime(target_year, target_month, 1)
    # Get the last day of the month
    last_day = first_day.replace(day=28) + timedelta(days=3) # Every month has 28 days, so adjust for the rest using timedelta
        
    # Generate a list of all the days in the month
    all_dates_in_month = [
      (first_day + timedelta(days=i)).strftime("%Y-%m-%d")
      for i in range((last_day - first_day).days + 1)
    ]
    
    return all_dates_in_month
        
  def display_calendar(self, calendar_days_formatted, highlight_color):     
    # Display calendar header
    print(f"{self.color_text(f"|Mo|Tu|We|Th|Fr|Sa|Su|", 'BG_BRIGHT_' + highlight_color, True)}")
    print(f"{self.color_text(f"|--|--|--|--|--|--|--|", 'BRIGHT_' + highlight_color, True)}")
    
    # Display calendar days with proper formatting
    for i in range(0, len(calendar_days_formatted), 7):
      print("".join(f" {day}" for day in calendar_days_formatted[i:i + 7]))
    
    print("")
    
    # Prompt user to continue so that they can see the calendar
    input(f"Press {self.color_text('any key', 'BRIGHT_YELLOW', True)} to {self.color_text('continue', 'BRIGHT_YELLOW', True)}: ")
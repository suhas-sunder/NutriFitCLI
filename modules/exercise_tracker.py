
import os
from datetime import datetime
from colour_sequence import color_text

class ExerciseTracker:
  def __init__(self):
    pass

  def get_date(self):
    while True:
        entered_date = input("Enter the date (YYYY-MM-DD): ")
        try:
            valid_date = datetime.strptime(entered_date, "%Y-%m-%d")
            return valid_date
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
    
  
  def log_exercise(self, target_date):
    target_date = self.get_date()
    print("Date Entered:", target_date)
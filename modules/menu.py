from colour_sequence import color_text

class MainMenu:
  def __init__(self):
    self.title = "✨ NutriFitCLI ✨"
    self.border_text = "||============================||"
    self.border_text_2 = "--------------------------------"
    
  def display_header(self, emoji="   ", menu_text="", header_color="PURPLE", space_before_emoji="         "):
    header_text = "      " + self.title + "     "  
    
    # Display app title
    print(color_text(self.border_text,header_color, True))
    print("  " + color_text(header_text,"BG_BRIGHT_" + header_color, True, False))
    print(color_text(self.border_text,header_color, True))
    
    # Display menu title
    print(space_before_emoji + emoji + color_text(menu_text.upper() + " MENU",header_color, True, True) + color_text(":",header_color, True))
    
    print(color_text(self.border_text_2, header_color, True))
    
  def default_menu(self): 
    self.display_header("📜 ", "Main", "YELLOW") 
    menu_items = ["Add/Remove Food(s)      |", "Add/Remove Exercise     |", "Food Log                |", "Exercise Log            |", "Monthly Progress        |", "Weekly Progress         |", "Exit                    |"]
    
    # Apply color to each menu item and display it
    for index, item in enumerate(menu_items):
      print(color_text(f"|   {index + 1}. {item}", "YELLOW"))
        
    print(color_text(self.border_text_2, "YELLOW", True))   
       
    while True:
      # Prompt user for menu input
      menu_input = input(color_text("Type the", "PURPLE") + color_text(" menu # ", "YELLOW", True) + color_text("followed by ", "PURPLE") + color_text("enter key", "YELLOW", True) + color_text(":", "PURPLE"))
      try:
        # If input matches number in menu, return the number
        if(int(menu_input) in range(1, menu_items.__len__() + 1)):
          user_number = int(menu_input)
          return(user_number)
        else:
          # If the input is not in the range, display an error message
          print(color_text("Please enter a number between 1 and " + str(menu_items.__len__()) + "!", "RED")) 
      except ValueError:
          # If the input is not a number, display an error message
          print(color_text("Invalid input. Please enter a number.", "RED"))
    
  def food_log_menu(self):
    self.display_header("🍜 ", "Calorie", "RED", "        ") 
    
  def exercise_log_menu(self):
    self.display_header("👟 ", "Exercise", "GREEN", "        ") 
  
  
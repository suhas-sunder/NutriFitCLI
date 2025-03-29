from colour_sequence import color_text

class MainMenu:
  def __init__(self):
    self.title = "NutriFitCLI"
    
  def display(self):
    print(color_text("Welcome to the ","YELLOW") + color_text(self.title,"BLUE") + color_text(" Main Menu!","YELLOW"))
  
  
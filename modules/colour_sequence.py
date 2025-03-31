
#  Copyright 2025
#  Authors: Suhas Sunder - 100548159
#  Date: March 28, 2025
#  Title: NutriFitCLI (NutriFit Command Line Interface)
#  Description: Handles all logic with applying colours and formatting to displayed text

import json # Importing json module

# Load ANSI color codes from a JSON file
with open('data/ansi_colours.json') as file:
    ANSI_COLORS = json.load(file)
    
class ColorSequence:
    def __init__(self):
        pass

    def format_ansi(self, text):
        return text.replace("\\033", "\033")
    
    # Function to color text using ANSI escape sequences for colors
    def color_text(self, text, colour, bold=False, underline=False):        
        starting_colour_code = self.format_ansi(ANSI_COLORS.get(colour))
        underline_code=""
        bold_code=""
                
        reset_code = self.format_ansi(ANSI_COLORS.get("RESET"))
        
        if underline:
            underline_code += self.format_ansi(ANSI_COLORS.get("UNDERLINE"))

        if bold:
            bold_code += self.format_ansi(ANSI_COLORS.get("BOLD"))        
                                                                
        return f"{starting_colour_code}{underline_code}{bold_code}{text}{reset_code}"  
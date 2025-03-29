import json

# Load ANSI color codes from a JSON file
with open('data/ansi_colours.json') as file:
    ANSI_COLORS = json.load(file)
    
# Function to color text using ANSI escape sequences for colors
def color_text(text, colour):
    starting_colour_code = ANSI_COLORS.get(colour).replace("\\033", "\033")
    reset_code = ANSI_COLORS.get("RESET").replace("\\033", "\033")
                                               
    return f"{starting_colour_code}{text}{reset_code}"


  
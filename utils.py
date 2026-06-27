import re

def parse_ingredients(ingredients):
    return [ingredient.strip() for ingredient in re.split(',|;', ingredients)]
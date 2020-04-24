"""Returns city and country name"""
def city_country(city, country, population=''):
    """Returs city and country from inputted values"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

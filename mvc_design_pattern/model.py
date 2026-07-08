"""The model holds the data for the weather. This would typically be an API
endpoint. To simulate this, there is a simple dictionary and a constant loop
which updates weather states (every 30s for 10 min)"""

import random


class Model:
    def __init__(self):
        self.observers = []
        # Set defaults
        self.weather_states = {
            "London": "Sunny",
            "Birmingham": "Raining",
            "Manchester": "Ice",
            "Leeds": "Sunny",
            "Sheffield": "Raining",
            "Hatfield": "Foggy",
            "Bristol": "Snowing",
        }
        # Set weather options, and define which are critical
        self.weather_options = ["Sunny", "Raining", "Cloudy"]
        self.critical_weather = ["Ice", "Snowing", "Foggy"]
        self.critical = False

    def update_weather(self):
        '''Randomly update one of the cities to a new weather state.'''
        # Make a random selection of city and weather
        random_city = random.choice(list(self.weather_states.keys()))
        weather_choices = self.weather_options + self.critical_weather
        option_choice = random.choice(weather_choices)
        # Update the dict
        self.weather_states[random_city] = option_choice
        # Set a critical flag if the random weather state is a critical one
        if option_choice in self.critical_weather:
            self.critical = True
        event = f"Update: {random_city} updated to {option_choice}"
        # Notify all observers (the controller)
        for observer in self.observers:
            observer.update(event, self.critical)

    def add_observer(self, obs):
        '''Function to register new observers'''
        if obs not in self.observers:
            self.observers.append(obs)

    def remove_observer(self, obs):
        '''Function to remove an observer'''
        try:
            self.observers.remove(obs)
        except ValueError:
            pass

    def get_locations(self):
        '''Returns the list of locations for the dropdown.'''
        return list(self.weather_states.keys())

    def get_weather_for(self, location):
        '''Returns the weather state for a specific location
        (default is Unknown)'''
        return self.weather_states.get(location, "Unknown")

    def is_weather_critical(self, location):
        '''Check if the weather for a location is critical.'''
        weather = self.weather_states.get(location)
        return weather in self.critical_weather

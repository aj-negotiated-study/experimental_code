'''The model holds the data for the weather. This would typically be an API
endpoint. To simulate this, there is a simple dictionary and a constant loop
which updates weather states.'''
import random


class Model:
    def __init__(self):
        self.observers = []
        self.weather_states = {"London": "Sunny",
                               "Birmingham": "Raining",
                               "Manchester": "Ice",
                               "Leeds": "Sunny",
                               "Sheffield": "Raining",
                               "Hatfield": "Foggy",
                               "Bristol": "Snowing"}

        self.weather_options = ["Sunny", "Raining", "Cloudy"]
        self.critical_weather = ["Ice", "Snowing", "Foggy"]
        self.critical = False

    def update_weather(self):
        random_city = random.choice(list(self.weather_states.keys()))
        weather_choices = self.weather_options + self.critical_weather
        option_choice = random.choice(weather_choices)
        self.weather_states[random_city] = option_choice
        if option_choice in self.critical_weather:
            self.critical = True
        event = "Update: {random_city} updated to {option_choice}"
        # Notify all observers
        for observer in self.observers:
            observer.update(event, self.critical)  # Now calls the method

    def add_observer(self, obs):
        if obs not in self.observers:
            self.observers.append(obs)

    def remove_observer(self, obs):
        try:
            self.observers.remove(obs)
        except ValueError:
            pass
    
    def get_locations(self):
        """Returns the list of locations for the dropdown."""
        return list(self.weather_states.keys())

    def get_weather_for(self, location):
        for key, value in self.weather_states.items():
            if key == location:
                state = value
        return state

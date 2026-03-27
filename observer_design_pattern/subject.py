'''The subject holds a list of observers and notifies them of any events.'''
import random


class WeatherSubject:
    def __init__(self):
        self.observers = []
        # Defining a list of weather events to simulate changes in weather
        self.events = ["It's sunny!",
                       "It's started to rain!",
                       "It's snowy!",
                       "It's cloudy and windy!",
                       "It's foggy!"]
        # Defining a list of critical weather events
        self.critical_events = ["Ice warning!", "Storm warning!"]

    def weather_update(self):
        '''Simulate a change in the weather'''
        self.critical = False
        self.all_events = self.events + self.critical_events
        event = random.choice(self.all_events)
        if event in self.critical_events:
            self.critical = True
        
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



'''The model. This is going to be the logic that receives weather updates. I have set up the model
as an observer in the observer pattern, which simulates it being the logic connected to a weather
API'''
from abc import ABC, abstractmethod
# from .controller import WeatherCategorisation


class Observer(ABC):
    @abstractmethod
    def update(self, message: str, location: str, critical: bool = False):
        """Called by the subject when an event occurs. Must be
        implemented by subclasses."""
        pass


class ModelWeatherObserver(Observer):
    def update(self, message: str, location: str, critical: bool = False):
            summary = (f"Weather update: {message}")
            criticality = critical
            if critical:
                location = (f"Please be careful in {location}")
            else:
                location = (f"Have a lovely day in {location}")


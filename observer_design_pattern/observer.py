'''This is our base observer, which will be notified of all subject events.'''
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str, critical: bool = False):
        """Called by the subject when an event occurs. Must be
        implemented by subclasses."""
        pass


class WeatherObserver(Observer):
    def update(self, message: str, critical: bool = False):
        if critical:
            pass
        else:
            print(f"Weather update: {message}")
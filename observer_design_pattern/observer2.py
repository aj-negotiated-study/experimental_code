'''This is our critical event observer, which will be notified
only of subject events which are on critical weather'''
from abc import ABC, abstractmethod
from observer import Observer


class WeatherObserver(Observer):
    def update(self, message: str, critical: bool = False):
        if critical:
            print(f"Critical alert: {message}")


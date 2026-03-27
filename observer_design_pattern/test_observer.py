#!/usr/bin/env python3
"""
Test script for the Observer design pattern implementation.
Demonstrates adding/removing observers and notifications.
"""

from subject import WeatherSubject
from observer import WeatherObserver as wo1
from observer2 import WeatherObserver as wo2

def test_observer_pattern():
    # Create the subject
    subject = WeatherSubject()

    # Create observers
    general_obs = wo1()
    critical_obs = wo2()

    print("=== Testing Observer Pattern ===")
    print(f"Initial observers: {len(subject.observers)}")  # Should be 0

    # Add observers
    subject.add_observer(general_obs)
    subject.add_observer(critical_obs)
    print(f"After adding observers: {len(subject.observers)}")  # Should be 2

    # Try adding the same observer again (should not duplicate)
    subject.add_observer(general_obs)
    print(f"After trying to add duplicate: {len(subject.observers)}")  # Should still be 2

    print("\n--- Simulating weather updates (with observers) ---")
    for _ in range(5):
        subject.weather_update()

    # Remove one observer
    subject.remove_observer(general_obs)
    print(f"\nAfter removing general observer: {len(subject.observers)}")  # Should be 1

    print("\n--- Simulating more updates (only critical observer) ---")
    for _ in range(5):
        subject.weather_update()

    # Remove the last observer
    subject.remove_observer(critical_obs)
    print(f"After removing critical observer: {len(subject.observers)}")  # Should be 0

    # Try removing a non-existent observer (should do nothing)
    subject.remove_observer(general_obs)
    print(f"After trying to remove non-existent: {len(subject.observers)}")  # Should still be 0

    print("\n--- Simulating updates with no observers ---")
    subject.weather_update()  # Should run without errors, just no notifications

    print("\nTest completed successfully!")

if __name__ == "__main__":
    test_observer_pattern()
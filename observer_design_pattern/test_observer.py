"""
Test script for the Observer design pattern implementation.
Demonstrates adding/removing observers and notifications.
"""

from subject import WeatherSubject
from observer import WeatherObserver as wo1
from observer2 import WeatherObserver as wo2
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def test_observer_pattern():
    """Function that runs through various tests
    for the system"""
    # Create the subject
    subject = WeatherSubject()

    # Create observers
    general_obs = wo1()
    critical_obs = wo2()

    print("Testing Observer Pattern")
    print(f"Initial observers: {len(subject.observers)}")  # Should be 0

    # Add observers
    subject.add_observer(general_obs)
    subject.add_observer(critical_obs)
    print(f"After adding observers: {len(subject.observers)}")  # Should be 2

    # Try adding the same observer again (should not duplicate)
    subject.add_observer(general_obs)
    print(
        f"After trying to add duplicate: {len(subject.observers)}"
    )  # Should still be 2

    # Test that weather updates are received and printed
    print("\nSimulating weather updates")
    for _ in range(5):
        subject.weather_update()

    # Remove one observer
    subject.remove_observer(general_obs)
    # Should be 1
    print(f"\nAfter removing general observer: {len(subject.observers)}")

    print("\nSimulating more updates (only critical observer present)")
    for _ in range(5):
        subject.weather_update()

    # Remove the other observer
    subject.remove_observer(critical_obs)
    # Should be 0
    print(f"After removing critical observer: {len(subject.observers)}")

    # Try removing a non-existent observer (should do nothing)
    subject.remove_observer(general_obs)
    print(
        f"After trying to remove non-existent: {len(subject.observers)}"
    )  # Should still be 0

    print("\nSimulating updates with no observers")
    # Should run without errors, just no notifications
    subject.weather_update()

    print("\nTest completed successfully!")


if __name__ == "__main__":
    test_observer_pattern()

"""Main script to start the program. It runs the view and
runs the model updating thread in the background"""

import tkinter as tk
import threading
import time
from model import Model
from controller import WeatherController
from view import WeatherView


def update_weather_background(model, duration=10 * 60, interval=30):
    '''Continuously update weather in the background for the specified
    duration, every 30 seconds.'''
    start_time = time.time()
    print("Starting background weather updates for 10 minutes...")

    while time.time() - start_time < duration:
        model.update_weather()
        # print(f"Weather updated: {model.weather_states}") ADD WHEN LOGGING
        time.sleep(interval)

    print("Background updates complete.")


if __name__ == "__main__":
    root = tk.Tk()

    # Create model and controller
    model = Model()
    controller = WeatherController(model)

    # Create view
    view = WeatherView(root, controller, model)
    controller.set_view(view)

    # Start background weather updates in thread
    update_thread = threading.Thread(
        target=update_weather_background,
        args=(model, 10 * 60, 30),
        daemon=True
    )
    update_thread.start()

    # Run the GUI
    root.mainloop()

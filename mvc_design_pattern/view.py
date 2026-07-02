'''The  view. This is going to be the logic that receives weather updates. I have set up the view to be
an observer of the model , which simulates it being the logic connected to a weather API'''
from abc import ABC, abstractmethod
# from .controller import WeatherCategorisation
import tkinter as tk
from tkinter import ttk
from model import Model
from controller import WeatherController


# class Observer(ABC):
#     @abstractmethod
#     def update(self, message: str, location: str, critical: bool = False):
#         """Called by the subject when an event occurs. Must be
#         implemented by subclasses."""
#         pass


# class ModelWeatherObserver(Observer):
#     def update(self, message: str, location: str, critical: bool = False):
#             summary = (f"Weather update: {message}")
#             criticality = critical
#             if critical:
#                 location = (f"Please be careful in {location}")
#             else:
#                 location = (f"Have a lovely day in {location}")

# Minimal Mock classes just to make the View load in isolation for testing
class MockModel:

    def get_locations(self):
        return ["London", "Manchester", "Leeds"]


class MockController:

    def handle_button_click(self):
        print("Button clicked!")


class WeatherView:

    def __init__(self, root, controller, model):
        self.controller = controller
        self.model = model

        root.title("Weather Updates")
        root.geometry("300x300")

        # A label acting as the message display
        self.label = tk.Label(
            root, text="Waiting for update...", wraplength=250, font=("Arial", 12)
        )
        self.label.pack(pady=40)

        # Dropdown Label
        self.combo_label = tk.Label(
            root, text="Select Location:", font=("Arial", 10)
        )
        self.combo_label.pack(pady=(20, 5))

        # Dropdown (Combobox) populated from Model
        self.location_var = tk.StringVar()
        self.combo = ttk.Combobox(
            root,
            textvariable=self.location_var,
            state="readonly",
            font=("Arial", 11),
        )
        self.populate_dropdown()
        self.combo.pack(pady=(0, 20))

        # A button that the user clicks
        self.button = tk.Button(
            root,
            text="Update weather",
            command=self.handle_user_inquiry,
            font=("Arial", 10),
        )
        self.button.pack()
    
    def populate_dropdown(self):
        self.combo["values"] = self.model.get_locations()
        if self.model.get_locations() and not self.location_var.get():
            self.combo.current(0)  # Default to first item initially

    def handle_user_inquiry(self):
        """User clicked 'Update Weather'.

        Ask controller/model to pull current status for selected dropdown city.
        """
        selected_location = self.location_var.get()
        if selected_location:
            weather_update = self.controller.show_weather_for_location(selected_location)
            message = f"The weather for {selected_location} is {weather_update}"
            self.label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    mock_model = Model()
    mock_controller = WeatherController(mock_model)

    # Instantiate the View so it actually builds the widgets on the root window
    view = WeatherView(root, mock_controller, mock_model)
    root.mainloop()
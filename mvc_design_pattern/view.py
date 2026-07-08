"""The  view. This is the logic that displays the weather
updates to the user. The controller passes
updates to the view and the view communicates button clicks (asking
for updates) from the user to the controller.
"""


import tkinter as tk
from tkinter import ttk
from model import Model
from controller import WeatherController


class WeatherView:
    '''This is the main view class, setting up the GUI.'''

    def __init__(self, root, controller, model):
        self.controller = controller
        self.model = model
        # Setting up the main Window
        root.title("Weather Updates")
        root.geometry("300x300")

        # A label displaying the weather update
        self.label = tk.Label(
            root, text="Waiting for update...", wraplength=250, font=("Arial",
                                                                      12)
        )
        self.label.pack(pady=40)

        # Dropdown Label for location selection
        self.combo_label = tk.Label(root, text="Select Location:",
                                    font=("Arial", 10))
        self.combo_label.pack(pady=(20, 5))

        # Locations are populated from the model
        self.location_var = tk.StringVar()
        self.combo = ttk.Combobox(
            root,
            textvariable=self.location_var,
            state="readonly",
            font=("Arial", 11),
        )
        self.populate_dropdown()
        self.combo.pack(pady=(0, 20))

        # Update weather button: this is the main input
        self.button = tk.Button(
            root,
            text="Update weather",
            command=self.handle_user_inquiry,
            font=("Arial", 10),
        )
        self.button.pack()

    # Calling get_locations from the model script to populate the dropdown
    def populate_dropdown(self):
        self.combo["values"] = self.model.get_locations()
        if self.model.get_locations() and not self.location_var.get():
            # Default to first item initially
            self.combo.current(0)

    def handle_user_inquiry(self):
        '''When the user requests a weather update, this function
        sends their location selection to the controller,
        which handles fetching and formatting the weather data.
        '''
        selected_location = self.location_var.get()
        if selected_location:
            message = self.controller.handle_location_request(
                selected_location)
            self.label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    model = Model()
    controller = WeatherController(model)

    # Instantiate the View
    view = WeatherView(root, controller, model)
    controller.set_view(view)
    root.mainloop()

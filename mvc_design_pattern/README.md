# Weather Updates Program: Model View Controller Version

## Project Structure

```
mvc_design_pattern/
├── model.py          
├── controller.py     
├── view.py          
├── main.py          
└── README.md        
```

## Components

### Model (`model.py`)

**Responsibility**: Store weather data and manage updates.

The model contains a dictionary of the default (starting) weather conditions for each of the locations. It also has lists of available weather statuses. The model script runs for 10 minutes in a separate thread, updating one of the locations to a new weather state at random every 30 seconds.

The model can be compared to the subject in the observer pattern. It has functions to register and remove observers.

### Controller (`controller.py`)

**Responsibility**: Mediator between Model and View.

The controller is an observer registered to the model. It processes data from the model to display in the correct format in the view. It also processes the button click from the user which triggers the display update in the view. This includes the logic to add an extra warning for the weather types under the 'critical' category.


### View (`view.py`)

**Responsibility**: Display UI and capture user input.

The view module is a Tkinter GUI which has a dropdown and a button. The dropdown is populated with the locations available (taken from the data in the model). The button is an update button; it triggers the controller action to give an update on the currently selected location.

### Main (`main.py`)

**Responsibility**: Initialize and orchestrate all components.

This script creates the instances of the model, view, and controller, and starts the thread for the model to run updates in the background.


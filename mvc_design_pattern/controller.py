"""The controller handles user actions and coordinates
between the model and view."""


class WeatherController:

    def __init__(self, model):
        self.model = model
        self.view = None
        # Register as an observer of the model
        self.model.add_observer(self)

    def set_view(self, view):
        '''Function called from the view script to set the view
        instance'''
        self.view = view

    def update(self, event, critical):
        '''Called by the model when weather updates occur.
        The controller acknowledges the update but doesn't automatically
        update the view. The user controls when to display via the button.
        '''
        pass

    def handle_location_request(self, location):
        '''Retrieves necessary information requested by the user
        and formats the message to return to the view.
        '''
        weather = self.model.get_weather_for(location)
        is_critical = self.model.is_weather_critical(location)

        message = f"The weather for {location} is {weather}"
        if is_critical:
            message += ". Be careful out there!"

        return message

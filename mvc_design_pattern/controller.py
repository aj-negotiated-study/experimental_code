'''The controller'''


class WeatherController:

    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def show_weather_for_location(self, location):
        """Pulls the current snapshot of a location from the Model

        and sends it directly to the View to display.
        """
        state = self.model.get_weather_for(location)
        return state
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mvc_design_pattern.model import ModelWeatherObserver
from subject import WeatherSubject
from observer import WeatherObserver as wo1
from observer2 import WeatherObserver as wo2


subject = WeatherSubject()
obs1 = wo1()
obs2=wo2()
model_obs = ModelWeatherObserver()

subject.add_observer(obs1)  # Adds obs1
subject.add_observer(obs2)
subject.add_observer(obs1)  # Does nothing (already added)
subject.add_observer(model_obs)

# subject.remove_observer(obs1)  # Removes obs1
# subject.remove_observer(obs1)  # Does nothing (already removed)
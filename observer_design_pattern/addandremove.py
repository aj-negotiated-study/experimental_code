from subject import WeatherSubject
from observer import WeatherObserver as wo1
from observer2 import WeatherObserver as wo2

subject = WeatherSubject()
obs1 = wo1()
obs2=wo2()

subject.add_observer(obs1)  # Adds obs1
subject.add_observer(obs2)
subject.add_observer(obs1)  # Does nothing (already added)

subject.remove_observer(obs1)  # Removes obs1
subject.remove_observer(obs1)  # Does nothing (already removed)
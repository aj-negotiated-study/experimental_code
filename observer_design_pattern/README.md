# Weather Updates Program: Observer Version

## Project Structure

```
observer_design_pattern/
├── subject.py           
├── observer.py          
├── observer2.py         
├── addandremove.py      
├── test_observer.py     
└── README.md           
```

## Components

### Subject (`subject.py`)

**Responsibility**: Maintain list of observers and notify them of events.

The subject script keeps a list of registered observers, and functions to add, remove, and send updates to them. It also has a list of defined critical and normal weather events.


### Observers
**Responsibility**: Respond to weather events.

**Observer.py**: This script contains the base class for an observer, and the first observer, which responds to regular weather events. The observer simply prints when there is an update.

**Observer2.py**: This script contains the critical weather events observer, which prints out when there are weather conditions that require warnings. It receives all weather events and takes no action for non-critical events.

**Output Example**:
```
Weather Update: It's Sunny!
Critical alert: Storm warning!
```

## Testing

### test_observer.py
This is the test script for the whole system. It creates subject and observer instances, demonstrates addition and deletion, and demonstrates weather updates.
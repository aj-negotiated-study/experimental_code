# Experimental Code: Mock RESTCONF API for Network Device Management
This code mimics a RESTCONF API setup, utilising CRUD operations on (mock) network devices for the purpose of configuration management through REST APIs.

It was also used as a way of testing the use of:
- Black formatter
- Flake8 linter
- Pytest

## Project Structure
```
restconf_api/
├── dev_configs.py    
├── handlers.py        
├── app.py            
├── test_api.py       
└── README.md          
```

The **dev_configs** file contains the expected format for the data- both for the device information and the format of the device configuration.
The **handlers** script is the majority of the logic. It contains all of the processes necessary for each of the API calls.
The **app** script is the Flask API logic. It defines each of the calls and their endpoints, uses the functions in the **handlers** script and ensures that outputs are in correct JSON format.
The **test_api** script is the test suite, containing unit tests for every API endpoint along with integration tests.

## Testing
The project includes 18 comprehensive unit tests covering pass and failsafe cases for each of the endpoint types, and integration tests for the whole system.

**Pytest Coverage Report:** 99% (handlers.py 100%, app.py 98%)


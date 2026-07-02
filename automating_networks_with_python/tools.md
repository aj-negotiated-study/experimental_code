# CLI Based Tools
This file details notes from the 'Automating Networks with Python' Pluralsight course

## Python for Network Applications
Helpful tools include:

- Paramiko: A library that implements the SSHv2 protocol, allowing encrypted network connections between devices
- Python debugger (pdb): Allows you to create breakpoints for debugging code

## Automating Networks with Paramiko and Netmiko
Tools:

- Paramiko (detailed above)
- Netmiko: An open-source SSH client configured for networks
- Jinja2: Used for templating text

### Infrastructure as Code
Core Concepts:

- Declaring the desired state of the network
- Abstraction of solutions from target systems (creating repeatable frameworks)
- Version control

**Idempotent**: Property defining an operation that can be executed many times and not make
unnecessary changes after the initial setup.

#### Jinja2
Key concepts:
- Intuitive text templating
- Includes many programming features
- Tight integration with any python-based project, including python-based frameworks like
Ansible

### Netmiko
This is Paramkiko based, and is a network-focused wrapper for it. It has wide platform support,
with 10 platforms with extensive use (as of 2022). 

Netmiko can replace paramiko, and in doing so the codebase is heavily reduced. This is because
it does a lot of the necessary steps in the background, making the manual configuration process
smoother.

Netmiko can be used for file transfer between network devices, which is useful for uploading
new software, updating configs etc.

**Comparing Paramiko and Netmiko**
- Paramiko supports SSH client or server, but Netmiko only supports client behaviour
- SSH access can use raw strings and low-level manual work, netmiko uses built-in helper functions
- Paramiko requires that quirks of individual platforms are manually accounted for, netmiko automatically handles many CLIs
- Paramiko uses a relatively basic API, netmiko includes advances features such as file transfer

## Responsibly Parsing Text Using Python
This is important for creating machine-readable configurations for use in Infrastructure as Code.

**Regular Expression (Regex)**: A pattern to be searched within a larger block of text
Regular expressions can extract data, and can be used to verify that input text follows a specified pattern.

**Unit Testing**: Passing static data to individual code modules for the purpose of testing them before they handle live data or interact with actual network devices. Pytest is a module commonly used for unit testing in python.

## Abstraction with NAPALM
**NAPALM stands for Network Automation and Programmability Abstraction Layer with Multivendor support**
It has:
- Multi-vendor abstraction
- Advanced network operations
It is built on top of Netmiko for underlying SSH configurations.

NAPALM getters: using '.get' functions which will run the underlying calls without having to do extensive manual work

NAPALM has a config replace operation, allowing an override of a current to desired state. It also has a config rollback (as long as SSH connectivity isn't lost), which is helpful if errors occur during implementation. 

The 'with' statement in python can wrap around the entire NAPALM process, removing the need for manual opening and closing of connections.

## Set Theory
A set is an unsorted collection of unique elements.
A set is in the following format:
```
my_set = {"item1", "item2", "item3"}
my_numerical_set= {1,2,3}
```

Set theory can be used in configuration by gathering all parameters (without duplicates) and performing *want - have* calculation. It is important to remember to convert to a set for the calculations and back to the original format after testing. 

Set theory can be combined with NAPALM, where set theory is used to compare current to desired state, and NAPALM configures and applies the necessary changes. 

### Comparing NAPALM to Netmiko and Paramiko
When NAPALM uses SSH to manage devices, it is relying on Netmiko to do so.
On top of Netmiko's functionalities, NAPALM adds:
- Config merge/replace/commit/discard/rollback
On top of paramiko's functionalities, Netmiko adds:
- Handling lower-level SSH
- Simplified interaction with network devices
- File transfer
Paramiko is relatively basic and provides 'no frills' send-and-recieve techniques for interaction with network devices. It is much more manual than the more abstract alternatives.

## Nornir
Basic Components:
- Config file: defines global runtime settings
- Inventory files: a pair of files (hosts.yml and groups.yml) which enumerate all hosts and groups. Groups files allows specification of group name, sub groups, and information about the groups. Hosts.yml includes root level device names, and then hostnames which specify IP/DNS, follwed by information.
- Variables
- Runbook: ties everything together

NAPALM can be used along with Nornir, for example .get() to find the information about hosts/groups

**Important imported function is InitNornir, which enables a lot of the functionality**
```
from nornir import InitNornir

nornir = InitNornir()
```
**there is an automatic nornir.log file which is written to when commands are executed, which is useful for debugging**

### Comparing Ansible and Nornir
| Ansible | Nornir |
|----------------|-------------|
|Yaml based DSL|Pure python|
|Playbooks, plays, and tasks|arbitrary flow (more freedom)|
|absible-specific DSL debugger|well-known python pdb|
|faster start up for beginner|goes further than ansible with more experience|

# APIs- The Modern Solution
**Application Programming Interfaces are sets of operations built for standardised management of network devices**
Advantages:
- simplified implementation
- structured data
- standardised abstraction (removing the need for specific CLI commands in templates)

## NETCONF
NETCONF uses SSH for transport between a client and a server. RPCs are standardised APIs used by clients to get configurations and other requested data from the server.

YANG is a C-style modelling language used to identify the structure that data should have. It can be used to show how data should be modelled when being transported and used by NETCONF client/servers.

NETCONF can be used with Nornir, Jinja2, and Netmiko.

## RESCONF
RESTCONF is stateless, based on HTTP. This makes it simple, as commands such as HTTP GET can be used to extract specific data from a specific URL.

# Writing Production-Grade Python Code
## Version Control
Git is a key tool for version control. It allows 'time travel' through code- going back to a stable version, merging development branches from multiple features together, and versioning the overall system.

## Embedded Error-Checking in Python
Example areas that need error checking:
- File input/output
- CLI arguments (input validation)
- Arithmetic
- Parsing (accuracy, and that is it actually done)
- Communications between components, especially with data transfer
- Format/structure of data

One activity that can be used is putting simple pre-checks before __main__ is run, which will run the checks before the file is executed in the command line. These errors could be e.g. the existence of an input file, arg numbers.

## Formatters
Formatters 'beautify' code. They help to eliminate 'snowflake' code, making all the code uniform without changing how it runs, which helps with projects that have multiple developers. It also allows uniformity across multiple projects. There are not many features by design, and it is useful to keep things simple. However, some formatters will allow customisation.

An example python formatter is black. This can be used to show the differences between files, or run ```black [filename]``` to re-format a file.

## Linters
Linters scan code to report on syntax and styling issues. This is useful for catching errors quickly before code is executed. They often run in seconds and provide detail on what and where issues exist. There are linters for many languages. For python, the common ones are Flake8 and Pylint.

## Writing Makefiles
Makefiles are dependency-aware build tools used in many languages for compiling. They are useful for efficient compiling as they only compile code that has changed. For python, a specific build sequence won't always make sense, but Makefiles can be used to break up execution phases and create different Makefile "targets" for different tasks. ```make lint``` or ```make test``` can be used to carry out specific actions on the code, and ```make all``` can be used to automate all of the pre-execution activities.
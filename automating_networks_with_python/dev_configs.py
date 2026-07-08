'''This file contains all of the data structures representing the
different devices on the network. Thisis to mimic YANG format.'''


class Device:
    def __init__(self, id, hostname, ip_address):
        self.id = id
        self.hostname = hostname
        self.ip_address = ip_address
        self.config = Config()


class Config:
    def __init__(self):
        self.interfaces = {}
        self.routing = {}
        self.vlans = []

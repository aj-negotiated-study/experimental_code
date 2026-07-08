"""This file contains all of the functions for data handling."""
from dev_configs import Device


class Handlers:
    def __init__(self):
        self.devices = {}
        self.next_id = 1

    def get_devices(self, id: str = "all"):
        '''This function returns device information.
        It takes the parameter 'id', which can be a
        specific device ID or "all"'''
        if id == "all":
            return self.devices
        else:
            return self.devices.get(id)

    def create_device(self, hostname, ip):
        '''Create a new device'''
        device = Device(
            id=self.next_id,
            hostname=hostname,
            ip_address=ip
        )

        self.devices[self.next_id] = device
        self.next_id += 1
        return device

    def update_device_config(self, device_id, config_data):
        '''Update a device's configuration.'''
        device = self.devices.get(device_id)
        if not device:
            return None

        if "interfaces" in config_data:
            device.config.interfaces = config_data["interfaces"]
        if "routing" in config_data:
            device.config.routing = config_data["routing"]
        if "vlans" in config_data:
            device.config.vlans = config_data["vlans"]

        return device

    def delete_device(self, device_id):
        '''Delete a device by ID.'''
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False

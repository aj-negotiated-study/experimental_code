"""This file implements Flask as the API methods"""

from flask import Flask, request, jsonify
from handlers import Handlers

app = Flask(__name__)
handler = Handlers()


def device_to_dict(device):
    '''This function formats device objects to a
    proper json payload'''
    return {
        "id": device.id,
        "hostname": device.hostname,
        "ip_address": device.ip_address,
        "config": {
            "interfaces": device.config.interfaces,
            "routing": device.config.routing,
            "vlans": device.config.vlans,
        },
    }


# GET ENDPOINTS
@app.route("/devices")
@app.route("/devices/<int:device_id>")
def get_devices(device_id=None):
    '''This returns either 1 device if an ID is specified, or all
    devices if no ID is specified'''
    if device_id is None:
        # Get all devices
        devices_dict = handler.get_devices(id="all")
        devices_list = [device_to_dict(d) for d in devices_dict.values()]
        return jsonify({"devices": devices_list}), 200
    else:
        # Get specific device
        device = handler.get_devices(id=device_id)
        if not device:
            return jsonify({"error": "Device not found"}), 404
        return jsonify(device_to_dict(device)), 200


# POST ENDPOINTS
@app.route("/devices", methods=["POST"])
def create_new_device():
    '''This identifies when a new set of information
    is submitted for creating a new device'''
    data = request.get_json()
    # Ensure all mandatory information is present
    if not data or "hostname" not in data or "ip_address" not in data:
        return jsonify({"error":
                        "Missing required fields: hostname, ip_address"}), 400

    device = handler.create_device(data["hostname"], data["ip_address"])
    return jsonify(device_to_dict(device)), 201


# PUT ENDPOINTS
@app.route("/devices/<int:device_id>/config", methods=["PUT"])
def update_config(device_id):
    '''Allows config for a specific device ID to be updated'''
    data = request.get_json()
    if not data:
        return jsonify({"error": "No config data provided"}), 400

    device = handler.update_device_config(device_id, data)
    if not device:
        return jsonify({"error": "Device not found"}), 404
    return jsonify(device_to_dict(device)), 200


# DELETE ENDPOINTS
@app.route("/devices/<int:device_id>", methods=["DELETE"])
def remove_device(device_id):
    '''Deleting a device by ID'''
    success = handler.delete_device(device_id)
    if not success:
        return jsonify({"error": "Device not found"}), 404
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)

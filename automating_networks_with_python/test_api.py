"""Unit & Integration Tests"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    '''Creating a test Flask client'''
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def fresh_handler():
    '''Reset handler between tests for test isolation,
    as each test gets its own handler'''
    from app import handler
    handler.devices = {}
    handler.next_id = 1
    return handler


# GET Endpoint Tests
def test_get_all_devices_empty(client, fresh_handler):
    '''Test GET /devices when no devices exist.'''
    response = client.get('/devices')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'devices' in data
    assert data['devices'] == []


def test_get_all_devices_with_data(client, fresh_handler):
    '''Test GET /devices with multiple devices.'''
    # Create some devices
    fresh_handler.create_device('device1', '192.168.1.1')
    fresh_handler.create_device('device2', '192.168.1.2')

    response = client.get('/devices')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['devices']) == 2
    assert data['devices'][0]['hostname'] == 'device1'
    assert data['devices'][1]['hostname'] == 'device2'


def test_get_specific_device(client, fresh_handler):
    '''Test GET /devices/{id} for a specific device.'''
    device = fresh_handler.create_device('device1', '192.168.1.1')
    device_id = device.id

    response = client.get(f'/devices/{device_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['hostname'] == 'device1'
    assert data['ip_address'] == '192.168.1.1'


def test_get_nonexistent_device_returns_404(client, fresh_handler):
    '''Test GET /devices/{id} returns 404 for non-existent device.'''
    response = client.get('/devices/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


# POST endpoint tests
def test_create_device(client, fresh_handler):
    '''Test that POST /devices creates a new device.'''
    response = client.post('/devices',
                           json={
                                'hostname': 'device1',
                                'ip_address': '192.168.1.1'
                            }
                           )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['hostname'] == 'device1'
    assert data['ip_address'] == '192.168.1.1'
    assert data['id'] == 1


def test_create_device_missing_hostname_returns_400(client, fresh_handler):
    '''Test POST /devices returns 400 when
    there is no hostname provided.'''
    response = client.post('/devices',
                           json={
                                'ip_address': '192.168.1.1'
                            }
                           )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_create_device_missing_ip_returns_400(client, fresh_handler):
    '''Test POST /devices returns 400 when ip_address is missing.'''
    response = client.post('/devices',
                           json={
                                'hostname': 'device1'
                             }
                           )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_create_device_no_data_returns_415(client, fresh_handler):
    '''Test POST /devices returns 415 when no data is provided.'''
    response = client.post('/devices')
    assert response.status_code == 415


def test_create_multiple_devices_have_unique_ids(client, fresh_handler):
    '''Test that  unique IDs are given when multiple
    new devices are created.'''
    device1 = fresh_handler.create_device('device1', '192.168.1.1')
    device2 = fresh_handler.create_device('device2', '192.168.1.2')

    assert device1.id != device2.id
    assert device1.id == 1
    assert device2.id == 2


# PUT endpoint tests
def test_update_device_config(client, fresh_handler):
    '''Test that PUT /devices/{id}/config
    successfully updates configuration.'''
    # Create a device
    device = fresh_handler.create_device('device1', '192.168.1.1')
    device_id = device.id

    config_data = {
        'interfaces': {
            'eth0': {'ip': '10.0.0.1', 'status': 'up'},
            'eth1': {'ip': '10.0.0.2', 'status': 'down'}
        },
        'routing': {
            'default_gateway': '10.0.0.254'
        },
        'vlans': [100, 200, 300]
    }
    # Update the config for that device
    response = client.put(f'/devices/{device_id}/config',
                          json=config_data
                          )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['config']['interfaces']['eth0']['ip'] == '10.0.0.1'
    assert data['config']['routing']['default_gateway'] == '10.0.0.254'
    assert 100 in data['config']['vlans']


def test_update_device_config_partial(client, fresh_handler):
    '''Test updating only some config fields.'''
    device = fresh_handler.create_device('device1', '192.168.1.1')
    device_id = device.id

    config_data = {
        'interfaces': {'eth0': {'ip': '10.0.0.1', 'status': 'up'}}
    }

    response = client.put(f'/devices/{device_id}/config',
                          json=config_data
                          )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['config']['interfaces']['eth0']['ip'] == '10.0.0.1'


def test_update_nonexistent_device_returns_404(client, fresh_handler):
    """Test PUT /devices/{id}/config returns 404 for non-existent device."""
    response = client.put('/devices/999/config',
                          json={'interfaces': {}}
                          )
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_update_device_config_no_data_returns_400(client, fresh_handler):
    '''Test PUT /devices/{id}/config returns 400 when
    there is no data provided.'''
    device = fresh_handler.create_device('device1', '192.168.1.1')
    device_id = device.id

    response = client.put(f'/devices/{device_id}/config', json={})
    assert response.status_code == 400


# DELETE endpoint tests
def test_delete_device(client, fresh_handler):
    '''Test that DELETE /devices/{id} removes a device.'''
    # Create, then delete new device
    device = fresh_handler.create_device('device1', '192.168.1.1')
    device_id = device.id

    response = client.delete(f'/devices/{device_id}')
    assert response.status_code == 204

    # Verify device has been deleted by expecting error code
    get_response = client.get(f'/devices/{device_id}')
    assert get_response.status_code == 404


def test_delete_nonexistent_device_returns_404(client, fresh_handler):
    '''Test DELETE /devices/{id} returns 404 for
    a non-existent device.'''
    response = client.delete('/devices/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_delete_device_from_multiple(client, fresh_handler):
    """Test deleting one device doesn't affect others."""
    device1 = fresh_handler.create_device('device1', '192.168.1.1')
    device2 = fresh_handler.create_device('device2', '192.168.1.2')

    # Delete device1
    response = client.delete(f'/devices/{device1.id}')
    assert response.status_code == 204

    # Device2 should still exist
    get_response = client.get(f'/devices/{device2.id}')
    assert get_response.status_code == 200
    data = json.loads(get_response.data)
    assert data['hostname'] == 'device2'


# Integration Testing
def test_create_update_retrieve_delete_workflow(client, fresh_handler):
    """Test complete CRUD workflow."""
    # Create
    create_response = client.post('/devices',
                                  json={'hostname': 'device1',
                                        'ip_address': '192.168.1.1'}
                                  )
    assert create_response.status_code == 201
    device_id = json.loads(create_response.data)['id']

    # Get
    get_response = client.get(f'/devices/{device_id}')
    assert get_response.status_code == 200

    # Put
    update_response = client.put(f'/devices/{device_id}/config',
                                 json={'interfaces': {'eth0':
                                                      {'ip': '10.0.0.1',
                                                       'status': 'up'}}}
                                 )
    assert update_response.status_code == 200

    # Verify put
    verify_response = client.get(f'/devices/{device_id}')
    data = json.loads(verify_response.data)
    assert data['config']['interfaces']['eth0']['ip'] == '10.0.0.1'

    # Delete
    delete_response = client.delete(f'/devices/{device_id}')
    assert delete_response.status_code == 204

    # Verify delete
    final_response = client.get(f'/devices/{device_id}')
    assert final_response.status_code == 404


def test_multiple_devices_isolation(client, fresh_handler):
    """Test that devices don't interfere with each other."""
    device1 = fresh_handler.create_device('device1', '192.168.1.1')
    device2 = fresh_handler.create_device('device2', '192.168.1.2')

    # Update device1 config
    client.put(f'/devices/{device1.id}/config',
               json={'interfaces': {'eth0': {'ip': '10.1.0.1',
                                             'status': 'up'}}}
               )

    # Check device2 config hasn't changed
    response = client.get(f'/devices/{device2.id}')
    data = json.loads(response.data)
    assert data['config']['interfaces'] == {}


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

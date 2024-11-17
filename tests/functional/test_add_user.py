




def test_auth_with_new_machine(client, init_data):
    init_data(username='test_user', password='test_pass')
    headers = {
        'SEEK_CUSTOM_AUTH': 'test_user:test_pass:' + 'a' * 64
    }
    response = client.get('/check', headers=headers)
    assert response.status_code == 201
    assert response.json['message'] == 'Machine added and authentication successful.'

def test_auth_with_existing_machine(client, init_data):
    user = init_data(username='test_user', password='test_pass', machine_id='a' * 64)
    headers = {
        'SEEK_CUSTOM_AUTH': f'test_user:test_pass:{user.machines[0].machine_id}'
    }
    response = client.get('/check', headers=headers)
    assert response.status_code == 200
    assert response.json['message'] == 'Authentication successful.'

def test_invalid_credentials(client, init_data):
    init_data(username='test_user', password='test_pass')
    headers = {
        'SEEK_CUSTOM_AUTH': 'test_user:wrong_pass:' + 'a' * 64
    }
    response = client.get('/check', headers=headers)
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid username or password.'

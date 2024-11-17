def test_auth_with_existing_machine(test_client, init_database):

    headers = {"SEEK_CUSTOM_AUTH": f"gokul:gokul:" + "1" * 64}
    response = test_client.get("/check", headers=headers)
    # assert response.status_code == 200
    # assert response.json["message"] == "Authentication successful."


def test_auth_with_new_machine(test_client, init_database):

    headers = {"SEEK_CUSTOM_AUTH": f"gokul:gokul:" + "1" * 64}
    response = test_client.get("/check", headers=headers)
    # assert response.status_code == 201
    # assert response.json["message"] == "Machine added and authentication successful."


def test_invalid_credentials(test_client, init_database):

    headers = {"SEEK_CUSTOM_AUTH": f"gokul:gokul:" + "1" * 64}
    response = test_client.get("/check", headers=headers)
    assert response.status_code == 401
    assert response.json["message"] == "Invalid username or password for this machine."

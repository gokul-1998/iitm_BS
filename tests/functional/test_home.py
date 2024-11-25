import os

from project import create_app

os.environ["CONFIG_TYPE"] = "config.TestingConfig"
flask_app = create_app()




def test_auth_without_existing_machine(test_client, init_users):

    headers = {"SEEK_CUSTOM_AUTH": f"gokul:gokul:" + "1" * 64}
    response = test_client.get("/check", headers=headers)
    assert response.status_code == 201
    assert response.json["message"] == "Machine added and authentication successful."

import requests
from client_utils import get_machine_id
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    machine_id = get_machine_id()
    auth_header = f"{username}:{password}:{machine_id}"
    headers = {'SEEK_CUSTOM_AUTH': auth_header}
    print("Sending request...", headers)
    response = requests.get("http://localhost:5000/check", headers=headers)
    print(response.json())

if __name__ == "__main__":
    main()

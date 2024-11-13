## Assignment Question for Backend Developer role at IITM - 2 to 4  years experience

1) Write a flask application which implements a custom authentication. This project will include two components - `a python file which sends requests to the server, henceforth known as the “desktop client”`, and `a flask server which processes these requests, henceforth known as the “backend server”`.


- The authentication credentials should be all sent in one header called SEEK_CUSTOM_AUTH
- The credentials should include three things. A username, a password, and a unique ID for a given machine. This unique machine ID should NOT be transferrable between computers.
- The first time the desktop client sends a request to the backend server, the backend server should associate the machine ID with the authenticated user. From now on, no other user should be able to use this machine ID.
The backend server has only one endpoint - /check - which returns OK if authentication successful, and returns the details of failure if authentication unsuccessful. Authentication is successful if either a user sends the correct username and password with a new machine ID (for the first time), or if a user already has a machine ID associated with them, they send the same machine ID with the correct username and password.
The client, when run, should accept the username and password from STDIN and send a request to /check if the backend, and print the response.
The backend should also have a command line utility to add a new user, and/or update an existing user's password.
Bonus points if you write a few automated tests (using pure python libraries).

Apart from this, the following criteria should also be met:

A README explaining how to run the code on a system having python3 and pip installed. You are only allowed to ask the tester to do a pip install and run python commands. The tester cannot do apt installs or similar system level installations.
All the code should be pushed onto a public GitHub repository.
The commits in the repository should be incremental (do not push all the code in one commit, it will be rejected), so we can gauge how you went about the problem by looking at the commit messages. Have sensible commit messages.

"""
This file (test_cli.py) contains the functional tests for the CLI (Command-Line Interface) functions.
"""


from project.models import User


def test_add_user(cli_test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'flask add-user' command is called with a username and password
    THEN check that the user is added successfully and handle duplicate users
    """
    username = "testuser"
    password = "securepassword"
    print("test_add_user")
    # Test adding a new user
    output = cli_test_client.invoke(args=['add-user', username, password])
    
    assert output.exit_code == 0
    assert f"Adding user... {username} {password}" in output.output

    # Test adding the same user again
    output_duplicate = cli_test_client.invoke(args=['add-user', username, password])
    
    assert output_duplicate.exit_code == 0
    assert f"Error: User '{username}' already exists." in output_duplicate.output

def test_update_user_password(cli_test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the 'flask update-password' command is called with a username and new password
    THEN check that the user's password is updated successfully
    """
    username = "testuser"
    new_password = "newsecurepassword"
    print("1"*20)
    # First, ensure the user exists before updating
    cli_test_client.invoke(args=['add-user', username, "initialpassword"])
    print("2"*20)
    output = cli_test_client.invoke(args=['update-password', username, new_password])
    print("3"*20)
    assert output.exit_code == 0
    assert f"Password updated for user '{username}'." in output.output
    
    # Optionally, verify that the password was actually updated in the database
    user = User.query.filter_by(username=username).first()
    assert user.check_password(new_password)  # Assuming you have a method to check passwords


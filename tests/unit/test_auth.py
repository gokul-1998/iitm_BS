
from project.auth_utils import is_valid_machine_id_format


def test_valid_machine_id():
    valid_id = "a" * 64
    assert is_valid_machine_id_format(valid_id) is True

def test_invalid_machine_id_non_hex():
    invalid_id = "z" * 64
    assert is_valid_machine_id_format(invalid_id) is False

def test_invalid_machine_id_length():
    invalid_id = "a" * 63
    assert is_valid_machine_id_format(invalid_id) is False

from unittest.mock import MagicMock
from project.auth_utils import validate_auth_header

def test_auth_header_missing():
    mock_request = MagicMock(headers={})
    user, message, status = validate_auth_header(mock_request)
    assert user is None
    assert message == 'Authorization header missing.'
    assert status == 401

def test_invalid_header_format():
    mock_request = MagicMock(headers={'SEEK_CUSTOM_AUTH': 'username:password'})
    user, message, status = validate_auth_header(mock_request)
    assert user is None
    assert message == 'Invalid header format. Expected format: username:password:machine_id'
    assert status == 400

def test_invalid_machine_id_format():
    mock_request = MagicMock(headers={'SEEK_CUSTOM_AUTH': 'username:password:invalid_machine_id'})
    user, message, status = validate_auth_header(mock_request)
    assert user is None
    assert message == 'Invalid machine ID format.'
    assert status == 400

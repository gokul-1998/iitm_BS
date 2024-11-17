import pytest
from flask import Request
from werkzeug.datastructures import Headers
from project.auth_utils import is_valid_machine_id_format, validate_auth_header


# Tests for `is_valid_machine_id_format`
def test_valid_machine_id():
    valid_id = "a" * 64
    assert is_valid_machine_id_format(valid_id) is True


def test_invalid_machine_id_non_hex():
    invalid_id = "z" * 64
    assert is_valid_machine_id_format(invalid_id) is False


def test_invalid_machine_id_length():
    invalid_id = "a" * 63
    assert is_valid_machine_id_format(invalid_id) is False


# Helper function to create a mock Flask request
def create_mock_request(headers=None):
    mock_request = Request.from_values(headers=Headers(headers))
    return mock_request


# Tests for `validate_auth_header`
@pytest.fixture
def mock_request_with_headers():
    def _create_request(headers):
        return create_mock_request(headers=headers)
    return _create_request


def test_auth_header_missing(mock_request_with_headers):
    mock_request = mock_request_with_headers(headers={})
    user, message, status = validate_auth_header(mock_request)
    assert user is None
    assert message == 'Authorization header missing.'
    assert status == 401


def test_invalid_header_format(mock_request_with_headers):
    mock_request = mock_request_with_headers(
        headers={'SEEK_CUSTOM_AUTH': 'username:password'}
    )
    user, message, status = validate_auth_header(mock_request)
    assert user is None
    assert message == 'Invalid header format. Expected format: username:password:machine_id'
    assert status == 400


def test_invalid_machine_id_format(mock_request_with_headers):
    mock_request = mock_request_with_headers(
        headers={'SEEK_CUSTOM_AUTH': 'username:password:invalid_machine_id'}
    )
    user, message, status = validate_auth_header(mock_request)
    assert user is None
    assert message == 'Invalid machine ID format.'
    assert status == 400

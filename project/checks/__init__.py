"""
The books Blueprint handles the creation, modification, deletion,
and viewing of books for the users of this application.
"""

from flask import Blueprint

checks_blueprint = Blueprint("checks", __name__)

from . import routes

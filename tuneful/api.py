import os.path
import json

from flask import request, Response, url_for, send_from_directory
from werkzeug.utils import secure_filename
from jsonschema import validate, ValidationError

from . import models
from . import decorators
from . import app
from .database import session
from .utils import upload_path

@app.route("/api/list", methods=["GET"])
@decorators.accept("application/json")
def music_get():
    """Pulls playlist of music"""
    music = session.query(models.music).all()
{
    "file": {
        "id": 7
    }
}

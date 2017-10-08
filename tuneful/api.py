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

@app.route("/api/music", methods=["GET"])
@decorators.accept("application/json")
def music_get():
    """Pulls playlist of music"""
    music = session.query(models.music).all()
    
    """Converts data to JSON and returns result"""
    data = json.dumps([post.as_dictionary() for post in posts])
    return Response(data, 200, mimetype="application/json")
    
@app.route("/api/music", methods=["POST"])
@decorators.accept("application/json")
def music_post():
    """Adds music to playlist"""
    music = session.query(models.music).get(id)
    
@app.route("/api/music/<int:id>", methods=["GET"])
@decorators.accept("application/json")
#    music = session.query()

@app.route("/music/<int:id>", methods=["GET"])
def unique_id(id):
    entry = session.query(Entry).filter(Entry.id == id).first()
    return render_template("music.html", entry=entry
    )

#{
#    "file": {
#        "id": 7
#    }
#}
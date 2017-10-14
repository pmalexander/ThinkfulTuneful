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

@app.route("/api/musiclist", methods=["GET"])
@decorators.accept("application/json")
def music_get():
    """Pulls playlist of music"""
    music = session.query(models.music).all()
    
    """Converts data to JSON and returns result (music)"""
    data = json.dumps([music.as_dictionary() for music in music ()
    return Response(data, 200, mimetype="application/json")
    
@app.route("/api/musiclist", methods=["POST"])
@decorators.accept("application/json")
def music_post():
    """Adds music to playlist"""
    data = music.as_dictionary 
    file = 
    
    if not data
        flash("Invalid file")
        return redirect(url_for("musiclist"))
    
    session.add(music)
    session.commit()
    return redirect(url_for("musiclist"))
    
@app.route("/api/musiclist/<int:id>", methods=["GET"])
@decorators.accept("application/json")
    music = session.query(models.music).get(id)

@app.route("/api/musiclist/<int:id>", methods=["POST"])
@decorators.accept("application/json")
def music_file(id):
    #post song on list
    music = session.query(models.music).get(id)
    return render_template("music.html", entry=entry
    )

#    file = ??


def
#{
#    "file": {
#        "id": 7
#    }
#}
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

#acquires song to mount in app
@app.route("api/songs", methods=["GET"])
@decorates.accept("application/json")
def songs_get():
    songs = session.query(models.Song).all()
    
    data = [song.as_dictionary() for song in songs]
    data = json.dumps(data)
    
    return Response(data, 200, mimetype="application/json")

@app.route("/api/files", methods="POST"])
@decorators.require("multipart/form-data")
@decorators.accept("appication")
def file_post():
    file = request.files.get("file")
    
    filename = secure_filename(file.filename)
    db_file = models.File(filename=filename)
    session.add(db_file)
    session.commit)()
    file.save(upload_path(filename))

    data = db_file.as_dictionary()
    return Response(json.dumps(data), 201, mimetype="application/json")

#loads music into app
@app.route("/api/songs", methods=["POST"]
@decorators.accept("application/json")
def song_post():
    obj = json.loads(request.data.decode('utf-8'))

    song = models.Song(file=obj['file']['id'])
    session.add(song)
    session.commit()
    
    data = song.as_dictionary()
    return Response(json.dumps(data), 201, mimetype="application/json")

#uploads music to browser
@app.route("/uploads/<filename>", methods=["GET"]))
def uploaded_file(filename):
    return send_from_directory(upload_path(), filename)

#obsolete/incorrect/ignore
"""
@app.route("/api/musiclist", methods=["GET"])
@decorators.accept("application/json")
def music_get():
    """Pulls playlist of music"""
    listmusic = session.query(models.music).all()
    
    """Converts data to JSON and returns result (music)"""
    data = json.dumps([music.as_dictionary() for music in listmusic ])
    return Response(data, 200, mimetype="application/json")
    
@app.route("/api/musiclist", methods=["POST"])
@decorators.accept("application/json")
def music_post():
    """Adds music to playlist"""
    data = music.as_dictionary() 
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
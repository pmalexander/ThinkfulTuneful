#connects models to the created database
from .database import *
#url_for sets a hard location to set and pull the file
from flask import url_for

"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy import.orm import sessionmaker, relationship
"""

from .database import Base

#song class allows categorization of files used to directly reference specific files
class Song(Base):
    __tablename__ = "songs"
    
    id = Column(Integer, primary_key=True)
    file = Column(Integer, ForeignKey("files.id"))
    
    def as_dictionary():
        ret = { "id":self.id,
            "file": {
                "id": self.song.id,
                "name": self.song.filename
                }
            }
        return ret

#file class creates means to reference file data
class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True)
    filename = Column(String(1024))
    song = relationship("Song", backref="song")

    def as_dictionary(self):
        return { "id":self.id, "name":self.filename}

#should remove, redundant
"""
class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    body = Column(String(1024))
    
    def as_dictionary(self):
        music = {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
        return music
        
#reference on how to structure the class
{
    "id": 1,
    "file": {
        "id": 7,
        "name": "Shady_Grove.mp3"
    }
}
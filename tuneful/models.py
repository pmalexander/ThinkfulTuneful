from sqlalchemy import Column, Integer, String, Sequence

from .database import Base

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
{
    "id": 1,
    "file": {
        "id": 7,
        "name": "Shady_Grove.mp3"
    }
}
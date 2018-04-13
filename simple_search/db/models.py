import logging

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer


logger = logging.getLogger(__name__)

db = SQLAlchemy()


class TblTextContainer(db.Model):
    __tablename__ = 'tbl_text_container'
    __searchable__ = ('content', )

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, server_default=db.func.now())
    content = Column(String(1000), nullable=False)

    @classmethod
    def get_by_text(cls, text):
        if text:
            return cls.query.whoosh_search(cls.content.like(text)).all()
        else:
            return cls.query.all()

    @classmethod
    def add(cls, content):
        instance = cls(content=content)
        db.session.add(instance)
        db.session.commit()
        return instance

    def to_dict(self):
        return {
            'content': self.content
        }

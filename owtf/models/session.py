"""
owtf.models.session
~~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from owtf.db.model_base import Model
from owtf.lib import exceptions
from owtf.models.target import target_association_table


class Session(Model):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    active = Column(Boolean, default=False)
    targets = relationship("Target", secondary=target_association_table, backref="sessions")

    @classmethod
    def get_by_id(cls, session, id):
        if session_obj := session.query(Session).get(id):
            return session_obj.to_dict()
        else:
            raise exceptions.InvalidSessionReference("No session with id: {!s}".format(id))

    @classmethod
    def get_active(cls, session):
        return session.query(Session.id).filter_by(active=True).first()

    @classmethod
    def set_by_id(cls, session, session_id):
        query = session.query(Session)
        session_obj = query.get(session_id)
        if not session_obj:
            raise exceptions.InvalidSessionReference("No session with session_id: {!s}".format(session_id))
        query.update({"active": False})
        session_obj.active = True
        session.commit()

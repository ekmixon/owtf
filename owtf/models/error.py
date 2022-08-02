"""
owtf.models.error
~~~~~~~~~~~~~~~~~

"""
from owtf.lib.exceptions import InvalidErrorReference
from sqlalchemy import Boolean, Column, Integer, String

from owtf.db.model_base import Model
from owtf.db.session import flush_transaction


class Error(Model):
    __tablename__ = "errors"

    id = Column(Integer, primary_key=True)
    owtf_message = Column(String)
    traceback = Column(String, nullable=True)
    user_message = Column(String, nullable=True)
    reported = Column(Boolean, default=False)
    github_issue_url = Column(String, nullable=True)

    def __repr__(self):
        return "<Error (traceback='{!s}')>".format(self.traceback)

    @classmethod
    def add_error(cls, session, message, trace):
        obj = Error(owtf_message=message, traceback=trace)
        session.add(obj)
        session.commit()
        return obj.to_dict()

    @classmethod
    def get_error(cls, session, error_id):
        if error := session.query(Error).get(error_id):
            return error.to_dict()
        else:
            raise InvalidErrorReference("No error with id {!s}".format(error_id))

    @classmethod
    def delete_error(cls, session, id):
        if not (error := session.query(cls).get(id)):
            raise InvalidErrorReference("No error with id {!s}".format(id))
        session.delete(error)
        session.commit()

    def to_dict(self):
        obj = dict(self.__dict__)
        obj.pop("_sa_instance_state", None)
        return obj

    @classmethod
    def get_all_dict(cls, session):
        errors = session.query(Error).all()
        return [err.to_dict() for err in errors]

    @classmethod
    def update_error(cls, session, error_id, user_message):
        obj = session.query(Error).filter(id=error_id)
        if not obj:  # If invalid error id, bail out
            raise InvalidErrorReference("No error with id {!s}".format(error_id))
        obj.user_message = user_message
        session.merge(obj)
        session.commit()

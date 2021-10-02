from app.main import db
from sqlalchemy import Column, Integer, String


class Test(db.Model):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    lastname = Column(String(45))

    def __repr__(self):
        return '<Test {}>'.format(self.name)

    @staticmethod
    def get_by_id(id):
        return Test.query.get(id)

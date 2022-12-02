from sqlalchemy import Column, Float, Integer, String, SmallInteger
from sqlalchemy.orm import validates

from database import BaseModel
from geoalchemy2 import functions
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method



class Restaurant(BaseModel):
    __tablename__ = "restaurants"

    id = Column(String, primary_key=True)
    rating = Column(SmallInteger, default=0)
    name = Column(String, nullable=False)
    site = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone = Column(String)
    street = Column(String)
    state = Column(String)
    city = Column(String)
    lat = Column(Float)
    lng = Column(Float)

    @validates("email")
    def validate_email(self, key, address):
        assert "@" in address
        return address

    @hybrid_property
    def point(self):
        return functions.ST_MakePoint(self.lng, self.lat)

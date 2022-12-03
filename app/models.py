import uuid

from database import BaseModel
from geoalchemy2 import functions
from sqlalchemy import Column, Float, Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.orm import validates


class Restaurant(BaseModel):
    __tablename__ = "restaurants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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

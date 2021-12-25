#!/usr/bin/python3
"""
Amenity model module
"""
from models.base_model import (BaseModel, Base)
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity model
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
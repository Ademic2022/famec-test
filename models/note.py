from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import Column, String, Integer, DateTime, Text
from models.base_model import BaseModel, Base
from datetime import datetime
import models


class Note(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = "notes"
        __table_arg__ = {"mysql_default_charset": "latin1"}
        title   = Column(String(255), nullable=False)
        content = Column(Text, nullable=False)
         
    else:
        title = ""
        content = ""
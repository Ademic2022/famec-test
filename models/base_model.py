"""This is the base model class for FAMEC"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

time = "%Y-%m-%dT%H:%M:%S.%f"

# if models.storage_t == "db":
#     Base = declarative_base()
# else:
#     Base = object
Base = declarative_base() 
class BaseModel(Base):
    """ The basemodel class that all other classes will inherit from """
    __abstract__ = True  # Marks this class as abstract, preventing SQLAlchemy from creating a table for it

    id = Column(String(60, collation='utf8mb4_unicode_ci'), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


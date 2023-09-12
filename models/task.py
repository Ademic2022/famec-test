from models.base_model import BaseModel, Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer

from enum import Enum as PythonEnum

class Task(BaseModel, Base):
    """ Task model to describe the tasks for users"""
    if models.storage_t == "db":
        __tablename__ = "tasks"
        __table_args__ = {"mysql_default_charset": "latin1"}
        title = Column(String(255), nullable=False)
        description = Column(String(1000))
        due_date = Column(String(50))
        priority = Column(Integer, default=1)
        status = Column(Integer, default=0)
        
        # Define the foreign key relationship to the User model
        user_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('users.id'), nullable=False)
        # Create a many-to-one relationship to the User model
        family_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('families.id'), nullable=False)
        # Create a many-to-one relationship to the Family model
        user = relationship('User', back_populates='tasks', foreign_keys=[user_id])
        family = relationship('Family', back_populates='tasks', foreign_keys=[family_id])


    else:
        title = ""
        description = ""
        due_date = ""
        priority = ""
        status = ""

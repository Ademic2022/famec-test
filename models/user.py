from models.base_model import BaseModel, Base
from models.notification import Notification
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
import hashlib
from flask_login import UserMixin



class User(UserMixin, BaseModel, Base):
    """ Represent the user details for the user class"""
    if models.storage_t == "db":
        __tablename__ = 'users'
        __table_args__ = {"mysql_default_charset": "latin1"}
        firstname = Column(String(128), nullable=False)
        lastname = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        username = Column(String(128), nullable=False)
        address = Column(String(255), nullable=False)
        country = Column(String(30), nullable=False)
        state = Column(String(30), nullable=False)
        zipcode = Column(Integer(), nullable=False)
        birthday = Column(String(10), nullable=True)
        # Create a one-to-many relationship to the Task model
        tasks = relationship('Task', back_populates='user')
        # Create a many-to-one relationship to the User model to represent family owner
        family_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('families.id'), nullable=True)
        family = relationship('Family', back_populates='members', foreign_keys=[family_id])

        sent_notifications = relationship("Notification", foreign_keys=[Notification.sender_id], back_populates="sender")
        received_notifications = relationship("Notification", foreign_keys=[Notification.recipient_id], back_populates="recipient")

    else:
        email = ""
        password = ""
        username = ""
        firstname = ""
        lastname = ""
        address = ""
        birthday = ""
        
    def __init__(self, *args, **kwargs):
        """Initializes the user if a passwordis created
        or the user is updated"""
        if "password" in kwargs:
            kwargs["password"] = hashlib.md5(
                kwargs["password"].encode()).hexdigest()
            super().__init__(*args, **kwargs)
                           
    def save_pwd(self):
        """saving the password to the database after hashing it"""
        if "password" in self.__dict__:
            self.password = hashlib.md5(self.password.encode()).hexdigest()
            super().save()
    
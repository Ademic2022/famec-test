from sqlalchemy import Column, String, Integer, JSON
from models.base_model import BaseModel, Base
import models

class UserInfo(BaseModel, Base):
    """ user information  to specify the tpyes of house and other attributes
    """
    if models.storage_t == "db":
        __tablename__ = 'userinfo'
        __table_args__ = {"mysql_default_charset": "latin1"}
        id = Column(Integer, primary_key=True)
        house_type = Column(String(50))
        family_size = Column(Integer)
        family_information = Column(JSON)
        number_of_rooms = Column(Integer)
    else:
        id = ""
        house_type = ""
        family_size = ""
        family_information = ""
        number_of_rooms = ""
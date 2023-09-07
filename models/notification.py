from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean, ForeignKey
from models.base_model import BaseModel


class Notification(BaseModel):
    __tablename__ = 'notifications'
    __table_args__ = {"mysql_default_charset": "latin1"}
    
    sender_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('users.id'), nullable=False)
    recipient_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('users.id'), nullable=False)
    content = Column(String(255), nullable=False)
    is_read = Column(Boolean, default=False)
    family_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('families.id'), nullable=False)

    sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_notifications")
    recipient = relationship("User", foreign_keys=[recipient_id], back_populates="received_notifications")
    family = relationship("Family", back_populates="notifications")
        
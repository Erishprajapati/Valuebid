from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4, unique=True, index = True)
    username = Column(String, unique=True, nullable=False, index = True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable = False)
    is_active = Column(Boolean, default = True)
    role = Column(String, default="buyer")
    
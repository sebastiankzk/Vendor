from sqlalchemy import Column, String, Integer, CHAR, Boolean, ForeignKey
from app.models import Base
from app.models.user import User

class VendorProfile(Base):
    __tablename__ = "VENDOR_PROFILE"

    vendorProfileID = Column(Integer, primary_key=True)
    profileName = Column(String(100), nullable=False)
    address = Column(String(255), unique=True, nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    phone = Column(CHAR(8), unique=True, nullable=False)
    status = Column(Boolean, nullable=False)
    userID = Column(Integer, unique=True, nullable=False)

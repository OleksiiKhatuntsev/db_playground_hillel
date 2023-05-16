from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class RoleModel(Base):
    __tablename__ = "roles"
    role_id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(50))
    users = relationship("UserModel", back_populates="role")

    def __str__(self):
        return f"id = {self.role_id}, title = {self.title}"

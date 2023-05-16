from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from alchemy.models.role_model import RoleModel

Base = declarative_base()

class RoleModel(Base):
    __tablename__ = "roles"
    role_id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(50))
    users = relationship("UserModel", back_populates="role")

    def __str__(self):
        return f"id = {self.role_id}, title = {self.title}"


class UserModel(Base):
    __tablename__ = "users"
    user_id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(100))
    password = Column(VARCHAR(20))
    age = Column(INTEGER)
    role_id = Column(ForeignKey("roles.role_id"))
    role = relationship("RoleModel", back_populates="users")


    def __str__(self):
        return f"id = {self.user_id}, email = {self.email}, password = {self.password}, age = {self.age}, role = {self.role.title}, "

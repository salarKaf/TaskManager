from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Table
from db.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String ,primary_key=True)
    email = Column(String)
    password = Column(String)
    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, unique=True,  primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    is_concluded = Column(Boolean)
    timestamp = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="projects")
    members = relationship("ProjectMember", back_populates="project")
    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True , index=True)
    title = Column(String)
    description = Column(String)
    is_done = Column(Boolean)
    isAccepted=Column(Boolean)
    timestamp = Column(DateTime)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project', back_populates='tasks')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')


class ProjectMember(Base):
    __tablename__ = 'project_members'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    project = relationship("Project", back_populates="members")
    user = relationship("User")



class Notice(Base):
    __tablename__='notice'
    id=Column(Integer , primary_key=True , autoincrement=True , index=True)
    text=Column(String)
    isRead=Column(Boolean)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    task = relationship("Task")



class UserNotice(Base):
    __tablename__='userNotice'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    notice_id = Column(Integer, ForeignKey('notice.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    notice = relationship("Notice", back_populates="members")
    user = relationship("User")

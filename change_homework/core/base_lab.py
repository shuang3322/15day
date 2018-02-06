#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,ForeignKey,Table
from sqlalchemy.orm import relationship,sessionmaker

# engine = create_engine("mysql+pymysql://shuang:123456@10.77.100.9:3306/homeworkdb?charset=utf8",echo = True)
engine = create_engine("mysql+pymysql://shuang:123456@10.77.100.9:3306/homeworkdb?charset=utf8")

Base = declarative_base() #生成orm基类

student_m2m_Class = Table('student_m2m_Class', Base.metadata,
                        Column('student_id',Integer,ForeignKey('user.id')),
                        Column('class_id',Integer,ForeignKey('class_open.id')),
                        )


class User_lab(Base):
    '''基础用户表'''
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    password = Column(String(64))
    qq_num = Column(String(64))
    role_id = Column(Integer, ForeignKey("role.id"))
    role_key = relationship("Role", foreign_keys=[role_id])
    Class_name = relationship('Class',secondary=student_m2m_Class,backref='user')
    # def __repr__(self):
    #     return "<User(name='%s',  password='%s')>" % (
    #         self.name, self.password)
class Role(Base):
    '''基础角色表'''
    __tablename__ = 'role'  # 表名
    id = Column(Integer, primary_key=True)
    role_name = Column(String(32))
class Class(Base):
    '''基础班级信息表'''
    __tablename__ = 'class_open'  # 表名
    id = Column(Integer, primary_key=True)
    class_name = Column(String(32))
    open_time = Column(Date)
    run_work = Column(String(32))

class Class_record(Base):
    '''上课记录表'''
    __tablename__ = 'Class_record'  # 表名
    id = Column(Integer, primary_key=True)
    role_name = Column(String(32))
    teacher = Column(String(32))
    schooltime = Column(Date)
    Class_id = Column(Integer, ForeignKey("class_open.id"))
    class_id_key = relationship("Class", foreign_keys=[Class_id])
class Homework(Base):
    '''基础班级信息表'''
    __tablename__ = 'homework'  # 表名
    id = Column(Integer, primary_key=True)
    homeworke_name = Column(String(32))
    home_Class_id = Column(Integer, ForeignKey("class_open.id"))
    home_Class_key = relationship("Class", foreign_keys=[home_Class_id])
class Mark(Base):
    '''基础成绩表'''
    __tablename__ = 'mark'  # 表名
    id = Column(Integer, primary_key=True)
    mark_num = Column(Integer)
    student_id = Column(Integer,ForeignKey("user.id"))
    student = relationship("User_lab", foreign_keys=[student_id])
    homework_id = Column(Integer,ForeignKey("homework.id"))
    homework = relationship("Homework", backref="homework")
class Record_log(Base):
    '''上课日志'''
    __tablename__ = 'record_log'
    id = Column(Integer, primary_key=True)
    record_start = Column(String(32))
    student_id = Column(Integer,ForeignKey("user.id"))
    student = relationship("User_lab", foreign_keys=[student_id])
    class_record = Column(Integer,ForeignKey("Class_record.id"))
    record = relationship("Class_record", foreign_keys=[class_record])
Base.metadata.create_all(engine)  # 创建表结构
#

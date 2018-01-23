#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys
Path=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(os.path.dirname(Path))
sys.path.append(BASE_DIR)
from core import base_lab
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=base_lab.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
role_add1 = base_lab.Role(role_name="老师")
role_add2 = base_lab.Role(role_name="学生")
role_add3 = base_lab.Role(role_name="管理员")
Session.add_all([role_add3])  # 把要创建的数据对象添加到这个session里， 一会统一创建
Session.commit()  # 现此才统一提交，创建数据
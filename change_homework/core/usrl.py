#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys
Path=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(os.path.dirname(Path))
sys.path.append(BASE_DIR)
from core import base_lab
from sqlalchemy.orm import sessionmaker
class login():
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
    def return_live(self):
        try:
            Session_class = sessionmaker(bind=base_lab.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
            Session = Session_class()
            my_user = Session.query(base_lab.User_lab).filter_by(name=self.name).filter_by(password=self.passwd).first()
            return my_user.role_key.role_name
        except BaseException as Ever:
            print(Ever)
            return None
run_login = login('shuang','123456')
print("角色查询:",run_login.return_live())
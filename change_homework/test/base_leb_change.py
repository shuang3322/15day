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
user_add1 = base_lab.User_lab(name="shuang",password="123456",qq_num="403060467",role_id=1)
user_add2 = base_lab.User_lab(name="shuang1",password="123456",qq_num="403060461",role_id=2)
user_add3 = base_lab.User_lab(name="shuang2",password="123456",qq_num="403060462",role_id=2)
user_add4 = base_lab.User_lab(name="shuang3",password="123456",qq_num="403060463",role_id=2)
user_add5 = base_lab.User_lab(name="shuang4",password="123456",qq_num="403060464",role_id=2)
role_add1 = base_lab.Role(role_name="老师")
role_add2 = base_lab.Role(role_name="学生")
role_add3 = base_lab.Role(role_name="管理员")
Session.add_all([user_add1,user_add2,user_add3,user_add4,user_add5,role_add1,role_add2,role_add3])  # 把要创建的数据对象添加到这个session里， 一会统一创建
my_user = Session.query(base_lab.User_lab).filter_by(name="shuang1").first()
print(my_user.role_key.role_name)
Session.commit()  # 现此才统一提交，创建数据
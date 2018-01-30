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
'''新增人员信息和'''
# user_add1 = base_lab.User_lab(name="shuang",password="123456",qq_num="403060467",role_id=2)
# user_add2 = base_lab.User_lab(name="shuang1",password="123456",qq_num="403060461",role_id=1)
# user_add3 = base_lab.User_lab(name="shuang2",password="123456",qq_num="403060462",role_id=1)
# user_add4 = base_lab.User_lab(name="shuang3",password="123456",qq_num="403060463",role_id=1)
# user_add5 = base_lab.User_lab(name="shuang4",password="123456",qq_num="403060464",role_id=1)
# role_add1 = base_lab.Role(role_name="老师")
# role_add2 = base_lab.Role(role_name="学生")
# role_add3 = base_lab.Role(role_name="管理员")
# Session.add_all([user_add1,user_add2,user_add3,user_add4,user_add5,role_add2,role_add1,role_add3])  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.commit()  # 现此才统一提交，创建数据
''' 人员并关联已有课程'''
# user_class1 = Session.query(base_lab.Class).filter_by(class_name="python").first()
# user_class = Session.query(base_lab.Class).filter_by(class_name="linux").first()
# my_user = Session.query(base_lab.User_lab).filter_by(name="shuang1").first()
# my_user1 = Session.query(base_lab.User_lab).filter_by(name="shuang2").first()
# my_user2 = Session.query(base_lab.User_lab).filter_by(name="shuang3").first()
# my_user3 = Session.query(base_lab.User_lab).filter_by(name="shuang4").first()
# # print(user_class1.id,user_class1.id,my_user.id)
# my_user.Class_name = [user_class,user_class1]
# my_user1.Class_name = [user_class,user_class1]
# my_user2.Class_name = [user_class,user_class1]
# my_user3.Class_name = [user_class,user_class1]
# Session.merge(my_user)
# Session.commit()#数据提交
''' 新增人员关联并新增课程'''
# class_add1 = base_lab.Class(class_name="python",open_time="2018-1-29",run_work="36周")
# class_add2 = base_lab.Class(class_name="linux",open_time="2018-1-27",run_work="36周")
# user_add5 = base_lab.User_lab(name="shuang9",password="123456",qq_num="403060464",role_id=1)
# user_add5.Class_name = [class_add1,class_add2]
# Session.add(user_add5)
# Session.commit()
'''修改数据'''
# my_user = Session.query(base_lab.User_lab).filter_by(name="shuang1").first()
# my_user.role_id=1
'''增加作业'''
# class_id = Session.query(base_lab.Class).filter_by(class_name="python").first()
# print(class_id.id)
# class_id = Session.query(base_lab.Class).filter_by(class_name="python").first()
# print(class_id)
# homework = Session.query(base_lab.Homework).filter_by(home_Class_id=class_id.id).first()
# print(homework.class_name)
homework = Session.query(base_lab.Homework).all()
for item in homework:
    print(item.home_Class_key.class_name)
# add_homework = base_lab.Homework(homeworke_name = "week 1 day", home_Class_id = class_id.id )
# print()
# Session.add(add_homework)
# Session.merge(my_user)
# Session.merge(my_user)#煞星
# Session.commit()#数据提交
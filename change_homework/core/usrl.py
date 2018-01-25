#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys
Path=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(os.path.dirname(Path))
sys.path.append(BASE_DIR)
from core import base_lab
from sqlalchemy.orm import sessionmaker
class login():#账户密码确定
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
    def return_levele(self):
        try:
            Session_class = sessionmaker(bind=base_lab.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
            Session = Session_class()
            my_user = Session.query(base_lab.User_lab).filter_by(name=self.name).filter_by(password=self.passwd).first()
            return my_user.role_key.role_name,my_user.id
        except BaseException as Ever:
            print(Ever)
            return None,None
class UI_dict():#界面
    def __init__(self,role):
        self.studet_dict={
            "Pay homework" : "Pay_homework",
            "Check the grade" : "Check_the_grade",
        }
        self.teacher_dict= {
            "Management class" : "Management_class",
            "Add class record" : "Add_class_record",
            "Change the grade" : "Change_the_grade",
        }
        self.role = role
    def return_role_dict(self):
        if self.role == "老师":
            return self.teacher_dict
        else:return self.studet_dict


class Features():
    def __init__(self,id):
        self.id= id
    def Pay_homework(self):
        print("\033[1;31;40m用户id：%s \033[0m" % (self.id))

        print("Features:","Pay_homework")

    def Check_the_grade(self):
        #查看成绩
        print("Features:","Check_the_grade")

    def Management_class(self):
        #管理班级
        print("Features:","Management_class")

    def Add_class_record(self):
        #新增上课记录
        print("Features:","Add_class_record")

    def Change_the_grade(self):
        #批改作业
        print("Features:","Change_the_grade")

test = login("shuang1","123456")
s,my_id =test.return_levele()
# print("s",s,type(s))
ui = UI_dict(s)
ui_dict = ui.return_role_dict()
for key,item in ui_dict.items():
     print("**",key,"**",)
     # print("key_:",key,"<======>","item_:",item)
init_Features = input("输入功能").strip()
feas = Features(id=my_id)
print("init_Features :",init_Features,"ui_dict.get(init_Features) :",ui_dict.get(init_Features))
print(hasattr(feas, ui_dict.get(init_Features)))
if hasattr(feas, ui_dict.get(init_Features))is True:
    go_fcun = getattr(feas, ui_dict.get(init_Features))
    go_fcun()
else:
    print("输入错误：",init_Features)
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
            return None
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
            "Show grade":"Show_grade",
        }
        self.role = role
    def return_role_dict(self):
        if self.role == "老师":
            return self.teacher_dict
        else:return self.studet_dict


class Features():
    def __init__(self,id):
        self.id= id
        Session_class = sessionmaker(bind=base_lab.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
        self.Session = Session_class()
    def Pay_homework(self):#作业提交
        print("\033[1;31;40m用户id：%s \033[0m" % (self.id))
        my_user = self.Session.query(base_lab.User_lab).filter_by(id=self.id).first()
        # return my_user.Class
        for item in my_user.Class_name:
            print("%s *开班时间%s"%(item.class_name,item.open_time))
        put_work = input("提交作业").strip()
        my_put_work_class_id = self.Session.query(base_lab.Class).filter_by(class_name=put_work).first()
        my_put_work_id = self.Session.query(base_lab.Homework).filter_by(home_Class_id=my_put_work_class_id.id).first()
        mark_add =base_lab.Mark(student_id=self.id,homework_id=my_put_work_id.id)
        self.Session.add(mark_add)
        self.Session.commit()
    def Check_the_grade(self):#查看作业
        my_user = self.Session.query(base_lab.Mark).filter_by(student_id=self.id).all()
        for item in my_user:
            print("NO:%s 名字:%s 作业名:%s 成绩:%s" % (
                item.id, item.student.name, item.homework.homeworke_name, item.mark_num))
        # print("Features:","Check_the_grade")

    def Management_class(self):
        show_class = self.Session.query(base_lab.Class).all()
        for item in show_class:
            print("ID号：\033[1;31;40m ",item.id,"\033[0m 课程名",item.class_name)
        change_id = input("添加人员课程序号：").strip()
        print(change_id)
        show_studer = self.Session.query(base_lab.User_lab).filter_by(role_id="1").all()
        for item in show_studer:
            print("ID号:\033[1;34;40m%s\033[0m姓名:%s QQNUM:%s"%(item.id,item.name,item.qq_num))
        add_class_student_qq_num = input("添加人员qq号：").strip()
        add_class = self.Session.query(base_lab.Class).filter_by(id=change_id).first()
        add_student = self.Session.query(base_lab.User_lab).filter_by(qq_num=add_class_student_qq_num).first()
        add_student.Class_name.append(add_class)
        self.Session.merge(add_class)
        self.Session.commit()
        show_add_class = self.Session.query(base_lab.Class).filter_by(id=change_id).first()
        print("班级名：" ,show_add_class.class_name)
        for item in show_add_class.user:
            print(item.name)
        # print("Features:","Management_class")

    def Add_class_record(self):

        print("Features:","Add_class_record")

    def Change_the_grade(self):
        my_user = self.Session.query(base_lab.Mark).all()
        print("Features:","Change_the_grade")
        for item in my_user:
            if item.mark_num == None:
                print("NO:%s 名字:%s 作业名:%s 成绩:%s" % (
                    item.id, item.student.name, item.homework.homeworke_name, item.mark_num))
        change_mark_num = int(input("修改成绩序号").strip())

        mark_num = self.Session.query(base_lab.Mark).filter_by(id=change_mark_num).first()

        mark_num.mark_num = int(input("成绩:").strip())

        self.Session.commit()
        # print("my_user:",my_user.student.name,my_user.homework.homeworke_name)

    def Show_grade(self):
        my_user = self.Session.query(base_lab.Mark).all()
        for item in my_user:
            print("NO:%s 名字:%s 作业名:%s 成绩:%s" % (item.id, item.student.name, item.homework.homeworke_name, item.mark_num))

test = login("shuang","123456")
s,user_id =test.return_levele()
# print("s",s,type(s))
ui = UI_dict(s)
ui_dict = ui.return_role_dict()
for key,item in ui_dict.items():
     print("**",key,"**",)
     # print("key_:",key,"<======>","item_:",item)
init_Features = input("输入功能").strip()
feas = Features(user_id)
# print("init_Features :",init_Features,"ui_dict.get(init_Features) :",ui_dict.get(init_Features))
# print(hasattr(feas, ui_dict.get(init_Features)))
if hasattr(feas, ui_dict.get(init_Features))is True:
    go_fcun = getattr(feas, ui_dict.get(init_Features))
    go_fcun()
else:
    print("输入错误：",init_Features)
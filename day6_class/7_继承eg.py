#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class School(object):

	def __init__(self,name,addr ):
		self.name = name
		self.addr = addr
		self.students = []
		self.staffs = []

	def enroll(self,stu_obj):
		self.students.append(stu_obj)
		print("为学员 %s 办理注册手续" % stu_obj.name )

	def hire(self,staff_obj):
		self.staffs.append(staff_obj)
		print( "雇佣新员工 %s" % staff_obj.name )

class SchoolMember(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def tell(self):
		pass


class Teacher( SchoolMember ):
	def __init__(self,name,age,sex,salary,course ):
		super(Teacher,self).__init__(name,age,sex )
		self.salary = salary
		self.course = course

	def tell(self):
		print("""
			---- info of Teacher:%s ----
			Name   : %s
			Age    : %s
			Sex    : %s
			Salary : %s
			Course : %s
			""" % (self.name, self.name, self.age, self.sex, self.salary, self.course) )

	def teach(self):
		print( "%s is teaching course [%s]" %( self.name,self.course ))

class Student(SchoolMember):
	def __init__(self,name,age,sex,stu_id,grade):
		super(Student,self).__init__(name,age,sex )
		self.stu_id = stu_id
		self.grade = grade

	def tell(self):
		print("""
			---- info of Teacher:%s ----
			Name   : %s
			Age    : %s
			Sex    : %s
			Stu_id : %s
			Grade  : %s
			""" % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade ))

	def pay_tuition(self,amount):
		print("%s has paid tuition for $%s" % (self.name,amount))

school = School("清华大学","Beijing")
t1 = Teacher("hero",18,"man",2000000,"Linux")
t2 = Teacher("hero2",18,"man",200000,"python")
s1 = Student( "student1",18,"man","00001","python")
s2 = Student( "student2",18,"man","00002","Linux")

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
# 雇佣新员工 hero
# 为学员 student1 办理注册手续

print( school.students )
print( school.staffs )
# [<__main__.Student object at 0x0000001A2C855358>]
# [<__main__.Teacher object at 0x0000001A2C8552E8>]

t1.teach()
# hero is teaching course [Linux]

school.enroll(s1)
for stu in school.students:
	stu.pay_tuition(5000)
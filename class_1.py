#coding:utf-8
# 旧式类（经典类）
# class A:
#     '''
#     This is A
#     '''
#     pass
# # 实例化
# a = A()
# print type(A)#classibj   类
# print type(a)#instance  实例化对象
# print a.__class__  #用于显示它的类型
# print A.__doc__    #显示类文档

#新式类(和继承有关，object是当前类的父类)
# class B(object):
#     pass

class People():
    #赋值（不建议这么使用）
    #Name='cctv'
    #初始化函数，实现初始化操作
    #self  当前的类
    def __init__(self,name,sex,age):
        #初始化 类属性（变量）
        self.Name=name
        self.Sex=sex
        self.Age=age
        # print (self)
    #真正意义上的构造函数
    # def __new__(cls, *args, **kwargs):
    #     print(cls)
    #     print(args)
    #     print(kwargs)


fbb1=People('fbb','woman',30)
#调用类属性
print(fbb1.Age)
# b=B()
# print (type(b))

#类属性和实例属性
# class A():
#     x=7   #类属性,静态数据
#     def __init__(self):
#         # self.x=a #实例化属性
#         pass
#
# a=A()
# print (A.x)
# print (a.x)
# a.x=2
# a.y=A()
# print (A.x)
# print (a.x)
# print (a.y.x) #类外拓展，实例（对象）属性


#练习
#定义学生类
# class Student:
#     school='ibf'
#     def __init__(self,sno,name):
#         self.Sno=sno
#         self.Name=name
#
# stu1=Student(1,'f')
# Student.school='bf'
# stu1.school='beifeng'
# stu2=Student(2,'z')
# print (dir(Student))
# print (dir(stu2))  # 对象属性
# print (stu2.school)
# print (Student.__name__)
#特殊属性
# __doc__  文档
# __init__ 初始化
# __module__  类所属模块
# __name__   类名
# __dict__   等同于dir(object) ，显示类的所有属性

#self的作用
#self一个神器参数
class B():
    #self 接收实例化过程中传入的所有数据，这些数据是初始化函数后的参数导入的
    #self就是一个具体的示例
    #self 主内
    def __init__(self):
        self.Name='ibf'
        print (self)
        print (type(self))
    def get_name(self):
        print (self.Name)
    def show_name(self):
        return self.get_name()

#a 主外
a=B()
#object.attribute  对象.属性
print(a.Name)
a.get_name()
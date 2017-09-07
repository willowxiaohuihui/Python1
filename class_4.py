#coding:utf-8
#数据封装
#实例方法
# class C:
#     def __init__(self):
#         pass
#     #设置属性值,方法
#     def set_name(self,name):
#         self.N=name
#     #获取属性值，方法
#     def get_name(self):
#         return self.N
#
#
# obj_c=C()
# obj_c.set_name('fzj')
# #实例化对象调用实例方法
# print obj_c.get_name()
# # print obj_c.name

# 静态方法
class Student():
    count=0
    books={}

    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 装饰器，静态方法
    @staticmethod
    def printClassAttr():
        #操作做的是类属性
        #静态方法属于类的一种方法，只能操作类属性，并且没有参数限制以及不需要示例参数，和类参数
        print (Student.count)
        print (Student.books)
#
stu=Student('name',10)  #实例化
# #1.通过类名直接调用
Student.printClassAttr()
# #2.通过实例化对象调用
stu.printClassAttr()



#方法
'''#内置三个装饰器
1.静态方法   @staticmethod
2.类方法     @classmethod
3.属性           @property

#方法
1.实例方法，操作self实例参数，还能通过实例化对象调用方法
2.静态方法，操作类属性，能通过类名直接调用，也可以通过实例化对象调用
3.类方法，操作类属性，能通过类名直接调用，（也可以通过实例化对象调用），最好使用类名调用

类方法和静态方法区别
1.静态方法没有参数限制，不需要使用self或者cls。但是类方法要使用cls作为第一个参数
2.静态方法调用类属性，使用类名.属性。
     类方法调用类属性，使用cls.属性'''

#3.类方法
class School(object):
    #学生人数
    stu_num=0
    def __init__(self):
        pass

    #使用类方法装饰器
    @classmethod
    #cls 代表类本身
    def printClass(cls):
        print (cls.__name__)
        print (cls.__dict__)

#通过类名调用我们类方法
School.printClass() #类名调用
s=School()
s.printClass()  #实例化对象调用，最好使用类名调用
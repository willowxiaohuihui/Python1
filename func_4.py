#coding:utf-8
#装饰器
# def foo():
#     print ('i am foo')
def num():
    print("num")

# num()   # 函数就是变量
num = 1   # num的引用被指向1,不能再调用
#在方法被调用输出foo is runing ,结束时，输出foo end

#简单装饰器
# def show(func):
#     #装饰定义
#     def wrapper(*args,**kwargs):
#         print ('%s is runing'%(func.__name__))
#         func(*args,**kwargs)
#         print ('%s end'%(func.__name__))
#     return wrapper
#
# def foo1():
#     print ('i am foo1')
#
# foo1=show(foo1)
# foo1()

#练习
#装饰器语法糖
#执行打印时间差，并计算a+b总和一个操作
import time
# def deco(func):
#     def wrapper(a,b):
#        startTime=time.time()#返回秒
#        func(a,b)#睡眠，执行综合计算
#        endTime = time.time()
#        msecs=(endTime-startTime)*1000#差值毫秒形式显示
#        print (u'时间差为：%f ms' % msecs)
#     return wrapper

def deco(func):
    def wrapper(*args,**kwargs):
        print ('deco')
        func(*args, **kwargs)
        print ('deco end')
    return wrapper
def deco2(func):
    def wrapper(*args,**kwargs):
        print ('deco2')
        func(*args, **kwargs)
        print ('deco2 end')
    return wrapper

#等同于嵌套了deco(deco2(addFunc(a,b)))
# @deco
# @deco2
# def addFunc(a,b):
#     print ('start addFunc')
#     print ('Result:%d'%(a+b))
#     print ('end addFunc')
# addFunc(3,8)

#练习2
#传入一个列表，判断长度，生成状态值
#如果列表长度小于5，则状态值为1
#否则为2
#使用状态值传入一个函数内，函数内判断状态值，执行不同的操作
def len_list(func):
    def a(*args,**kwargs):
        #数据过滤一个过程
        if len(*args)<5:
            # print (kwargs)
            func(1)
            # func(1,1,*args)
        else:
            # func(2,2,*args)
            func(2)
    return a
@len_list
def go_list(num):
    print (num)
# def go_list(num,num2,list):   #python会自己判断你传入的数据是数字还是数列
#     print (num,num2,list)

go_list(range(9))
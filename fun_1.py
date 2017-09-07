#coding:utf-8
import math
#自定义一个函数
#封装我们质数判断
#return 结束函数，返回一个值或者多个值给调用方
# def _zhishu(num):
#     for i in range(2,int(math.sqrt(num))+1):
#         if num%i==0:
#             return 1
#     return 0
# #函数调用
# a=_zhishu(13)
# print a
#
# def returnMore():
#     return 1,2,3,4,5

# print returnMore()

#x=1,y=2请用三行语句交换他
#1.可以使用中间变量，暂时存储某个值
# x=1
# y=2
# temp=x
# x=y
# y=temp
# print x,y
#2.不使用中间值，直接交换
# x=1
# y=2
# x=x+y
# y=x-y
# x=x-y
# print x,y
#3.python的元组重置原理
# x=1
# y=2
# y,x=x,y
# print x,y
def returnMore():
    '''
    返回多个值
    :return: 1,2,3,4,5
    '''
    return 1,2,3,4,5
print (math.sqrt.__doc__)


#函数的结构
# def functionname(arg):
#     '函数_文档描述字符串'
#     函数主体部分
#     return (返回值)


def fun(a):
    return a**2

#传入两个参数，第一个参数表示函数名，第二参数表示值
def get_fun(f,num):
    return f(f(num)+1)

print (get_fun(fun,2))


#不可更改
b=2
def get_num(b):
    b=10
get_num(b)
print (b)  #2

#可更改
list1=[1,2,3]
def list3(list2):
    list2.append([1,2])

list3(list1)
print (list1)
#a. [1,2,3]
#b  [1,2,3,[1,2]]
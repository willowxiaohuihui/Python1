#coding:utf-8
#捕获异常
# try:
#     代码片段
# except <异常名>[,附加的数据]
#     异常处理

#1.可接受所有异常，使用BaseException
#2.else：假如上一层的except没有捕获到错误，所有正常操作和异常就会掉到else中去进行处理
# try:
#     f=open('2.txt','r')
#     f.write('Hello World')
# except RuntimeError:
#     print u'没有打开文件或者读取失败'
# except BaseException,e:
#     print e

#3.finally 无论上面执行了什么，都会执行finally
# try:
#     f=open('2.txt','w')
#     f.write('Hello World')
# except RuntimeError:
#     print(u'没有打开文件或者读取失败')
# except BaseException:
#     print(e)
# finally:
#     print('finally')



try:
    try:
        f=open('2.txt','r')
        f.write('Hello World')
    finally:
        print ('finally')
except RuntimeError:
    print (u'没有打开文件或者读取失败')
except BaseException as e:
    print (e)
    
try:
    num = int('abc')      #try里的代码是受保护的
    print(num)
except Exception as e:
    print(e)


#使用一个随机数模块，随机生成100个数，遍历数组，如果列表中出现10，则报异常
from random import *
list1=[]
for i in range(0,100):
    list1.append(randint(0,50))
if 10 in list1:
    #生成一个异常
    #raise
    #raise [exception name[,args]]
    try:
        raise Exception('having',3)
    except Exception,e:
        print 'having 10'


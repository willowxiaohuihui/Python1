#coding:utf-8
#引入math 数学计算模块
from math import *   # 可以直接使用sqrt()
#import math     # 要使用math.sqrt()

#1.判断一个数是否是质数（素数）
# break ,continue
#break 跳出（结束）循环
#continue 跳过当前循环，直接进入下一次循环
# for i in range(20):
#     if i==10:
#         continue
#     print i
# num=12
# s=0
# for i in range(2,13):
#     if num%i==0:
#         s=1
#         break
# if s==1:
#     print u'不是一个质数'
# else:
#     print (u'是一个质数')

#2.取出0-100中间所有质数
# for num in range(2,101):
#     #质数判断开始
#     # 判断是否是质数的状态值
#     s = 0
#     #循环遍历2~num-1,判断是否满足某个数能整除num
#     for i in range(2,num):
#         #判断能被整除，则设置s状态值为1，并且跳出循环
#         if num%i==0:
#             s=1
#             break
#     #输出满足条件的质数
#     if s==0:
#         print (num,)

#3.进行综合的计算
#定义一个列表，存储所有满足条件的质数
list2=[]
sum=0
for num in range(2,101):
    #质数判断开始
    # 判断是否是质数的状态值
    s = 0
    #循环遍历2~num-1,判断是否满足某个数能整除num
    for i in range(2,int(sqrt(num)+1)):
        #判断能被整除，则设置s状态值为1，并且跳出循环
        if num%i==0:
            s=1
            break
    #输出满足条件的质数
    if s==0:
        #print u'是一个质数',num
        sum+=num
#循环遍历列表，进行总计计算
# sum=0   #总计变量初始化
# for i in list2:
#     sum=sum+i
#     #等同于 sum+=i
# #输出最后的结果
print (u'0-100中间所有质数和为：',sum)
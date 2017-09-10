#!/usr/bin/python
#coding:utf8
"""
"""
# def jiecheng(number):
#     s=1
#     for i in range(1,number+1):
#         s=s*i
#     return s
#
# number=int(input('请输入你要求的输的阶乘：'))
# ss=jiecheng(number)
# print(ss)


#字符串
# def changdu(str_1):
#     list1=[]
#     for i in str_1:
#         list1.append('i')
#     return len(list1)
#
# str1=input('请输入字符串：')
# print(changdu(str1))




#完数
# for i in range(2,1000):
#     s = 0
#     for j in range(1,(i+2)//2):
#         # print(j)
#         if i%j==0:
#             # print(j)
#             s=s+j
#     if s==i:
#         print(i)

#完全平方数



#提成
# def ticheng(number):
#     sum_tc=0.0
#     if number<=10:
#         sum_tc=number*0.1
#         print(sum_tc)
#     elif number<=20:
#         sum_tc=10*0.1+(number-10)*0.075
#         print(sum_tc)
#     elif number<=40:
#         sum_tc=10*0.1+10*0.075+(number-20)*0.05
#         print(sum_tc)
#     elif number<=60:
#         sum_tc = 10 * 0.1 + 10 * 0.075 + 20*0.05+(number - 20) * 0.03
#         print(sum_tc)
#     elif number<=100:
#         sum_tc = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20*0.03+(number - 40) * 0.015
#         print(sum_tc)
#     else:
#         sum_tc = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 +40*0.015+ (number - 100) * 0.01
#         print(sum_tc)
# num=int(input('请输入你的利润：'))
# ticheng(num)

#9
# a=int(input('请输入一个数：'))
# n=int(input('请输入你要相加的数的个数：'))
# j=a
# k=len(str(a))
# print(k)
# s=0
# for i in range(1,n+1):
#     s+=a
#     print(s)
#     a=a*(10**k)+j
#
# print('你输入的数字是'+str(j)+'共有'+str(n)+'个数相加结果是:',s)


#5
# import math
# for i in range(1001):
#     m=i+100
#     n=m+168
#     if (math.sqrt(m)-int(math.sqrt(m)))*100==0 and (math.sqrt(n)-int(math.sqrt(n)))*100==0:  #主要用来判断完全平方数，开根号后没有小数
#         print(i)

    # if str(int(math.sqrt(m))).isdigit() and str(int(math.sqrt(n))).isdigit():
    #     print(i)

#找质因数

# def f(n):
#     list1=[]
#     if n == 1:
#         print('你输入的是1=1')  #如果输入的数是1，直接输出
#     else:
#         for i in range(2,n+1):
#             if n%i==0:
#                 list1.append(i)
#                 if i==n:  #如果i等于n时结束循环
#                     break
#                 else:
#                     n = n//i
#                     return f(n)
#     print('输出的质数是：',list1)
# n=int(input('请输入一个数：'))

def f(n):
    n=int(n)
    for i in range(2,n//2+1):
        if n%i==0:
            print (i,end='')
            print ("*",end='')
            return f(n//i)
    print (n,end=' ')
num=int(input('请输入一个正整数：'))
print('你输入的正整数的质因数分解为:')
print(f(num))

# n=num = int(input('请输入一个数字：'))  # 用num保留初始值
# f = []  # 存放质因数的列表
# for j in range(int(num / 2) + 1):  # 判断次数仅需该数字的一半多1次
#     for i in range(2, n):
#         t = n % i  # i不能是n本身
#         if t == 0:  # 若能整除
#             f.append(i)  # 则表示i是质因数
#             n = n // i  # 除以质因数后的n重新进入判断，注意应用两个除号，使n保持整数
#             break  # 找到1个质因数后马上break，防止非质数却可以整除的数字进入质因数列表
#
# if len(f) == 0:  # 若一个质因数也没有
#     print('该数字没有任何质因数。')
# else:  # 若至少有一个质因数
#     f.append(n)  # 此时n已被某个质因数整除过，最后一个n也是其中一个质因数
#     f.sort()  # 排下序
#     print('%d=%d' % (num, f[0]), end='')
#     for i in range(1, len(f)):
#         print('*%d' % f[i], end='')

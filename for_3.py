#coding:utf-8
#已知大公鸡5元，母鸡3元，小鸡1元，我有100块，可能买几只公鸡，几只母鸡，几只小鸡，把所有的可能都显示出来。
#i 表示公鸡，j表示母鸡，k表示小鸡
# for i in range(0,21):
#     for j in range(0,34):
#         for k in range(0,101):
#             #pass #空操作，占位
#             if 5*i+3*j+k==100:
#                 print u'公鸡有：%d只，母鸡有：%d只，小鸡有：%d只'%(i,j,k)

#百元买白鸡，已知大公鸡5元，母鸡4元，3只小鸡1元，我有100块要买100只鸡
#提问：可能买几只公鸡，几只母鸡，几只小鸡，把所有的可能都显示出来。
for i in range(0,21):
    for j in range(0,26):
        for k in range(0,101):
            #pass #空操作，占位
            if (5*i+4*j+k==round(100)) and (i+j+3*k==100):
                print u'公鸡有：%d只，母鸡有：%d只，小鸡有：%d只'%(i,j,k)


#coding:utf-8
#已知第一个数为1，第二个数为1，并且满足等式f(x)=sum(f)+f(x-1),请计算f(100)的值（斐波那契数列）
list1=[]
#追加序列
list1.extend([1,1])
#已得到2个数值，所以下标从2开始
# for i in range(2,100):
#     #计算当前列表值
#     list1.append(list1[i-1]+list1[i-2])
#     print list1[i]
# print ('f(10)为',list1[9])

n=int(input("请输入X的值："))
a=1
b=1
sum=0
for i in range(1,n-1):
    sum=a+b
    a=b
    b=sum
print(sum)


#coding:utf-8
#实现九九乘法表
#1.实现直角三角形的打印,输入一个数值（m），输出m行m列的三角形
# *
# **
# ***
# ****
# *****
#.....
#(1)获取输入的值
# num=int(input(u'请输入三角形的行数'))
# #i表示行数
# for i in range(num):
#     #j代表列数
#     print ('*'*(i+1))
# #2
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#外层for里面两个并列for,center(),两次字符串重复
#1.外层for里面两个并列for
num=int(input(u'请输入三角形的行数:'))
# #i代表行数
for i in range(0,num):
    #j 来控制打印倒三角，倒三角有空格组成，当前空格数量为总行数-当前行数
    for j in range(num-i):
        print ('',end=' ')
    # k 来控制打印'* '，当前输出的数量为行数（i+1）
    for k in range(i+1):
        print ('* ',end='')
    print()
for i in range(0,num):
    #j 来控制打印倒三角，倒三角有空格组成，当前空格数量为总行数-当前行数
    for j in range(1+i):
        print ('',end=' ')
    # k 来控制打印'* '，当前输出的数量为行数（i+1）
    for k in range(num-i):
        print ('* ',end='')
    print()
#2.center()
for i in range(num):
    str=''
    for k in range(i+1):
        str+='* '
    print (str.center(2*num))
# #3.两次字符串重复
for i in range(num):
    print (' '*(num-i)+'* '*(i+1))
for i in range(num):
    print(' '*(i+1)+'* '*(num-i))
#4.center+一次字符串重复
# for i in range(num):
#     print (str('* '*(i+1)).center(2*num))

#4。九九乘法表
#1*1=1
#2*1=2 2*2=4
#.......
#i 控制的行数，即乘数
# for i in range(1,10):
#     for j in range(1,i+1):
#         print ('%d*%d=%-2d'%(i,j,i*j),'\t',end='')
#     print()  #自动换行，因此不用加/n


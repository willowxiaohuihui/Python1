#coding:utf-8
#***递归
#1.设定出口，递归的最底层
#2.递归一定要有return
#1.f(x)=f(x-1)+f(x-2)
#出口 f(1)=1,f(2)=1
# 请使用函数形式表达f(x)
def f(x):
    # print(x)
    if x==1 or x==2:
        return 1
    else:
        return f(x-1)+f(x-2)
print (f(10))

#2.阶乘
#5!=5*4*3*2*1
# 输入一个数，显示他的阶乘结果
def g(x):
    if x==1:
        return 1
    else:
        return x*g(x-1)
print (g(5))


#请写出一段代码实现删除一个list里面的重复元素
# list1=[1,2,3,4,5,4,3,2,1]
# #print set(list1)
# #定义一个新的列表
# list2=[]
# #遍历列表
# for i in list1:
#     #判断list2中是否存在当前值
#     if i not in list2:
#         list2.append(i)
# print list2

#已知列表[123,123,13,546,312,63,124,61,37,1278,19320,10],请使用冒泡排序进行倒叙排序列表
#冒泡排序
#123,1221,21,2,23
#第一排序
#1221,123,21,2,23
#1221,123,21,2,23
#1221,123,21,2,23
#1221,123,21,23,2
#第二次排序
#1221,123,21,23,2
#1221,123,21,23,2
#1221,123,23,21,2
#第三次排序
#1221,123,23,21,2
#1221,123,23,21,2
#第四次排序
#1221,123,23,21,2
list2=[123,123,13,546,312,63,124,61,37,1278,19320,10]
list2_len=len(list2)
# #使用i控制排序次数
for i in range(0,list2_len-1):
    #使用 j 控制比较次数，并且使用j来控制，当前要比较的下标
    for j in range(0,list2_len-1-i):
        #判断当前项是否小于后一项，
        if list2[j]<list2[j+1]:
            #如果满足条件则进行交换
            list2[j],list2[j + 1]=list2[j+1],list2[j]
print (list2)

#选择排序
#123,1221,2,21,23
#第一次排序
#123,1221,23,21,2
#第二次排序
#123,1221,23,21,2
#第三次排序
#123,1221,23,21,2
#第四次排序
#1221,123,23,21,2

list2=[123,123,13,546,312,63,124,61,37,1278,19320,10]
#遍历列表
list_len=len(list2)
#控制排序次数
for i in range(list_len-1):
    # #遍历剩余的列表，找到列表中最小值的下标
    # min_index=0
    # #遍历确定当前范围的最小值的下标
    # for j in range(list_len-i):
    #     #比较最小值下标对应的值和当前项的值
    #     if list2[min_index]>list2[j]:
    #         #当前项小的话，min_index重新赋值
    #         min_index=j
    # #执行交换
    # list2[list_len-i-1],list2[min_index]=list2[min_index],list2[list_len-i-1]
    #使用分片原理，使min在指定范围内找到最小值
    #使用find定位最小值第一次出现的下标
    #使用min_index接收
    min_index=list2.index(min(list2[:list_len-i]))
    #使用last_index来接受最后一项的下标
    last_index=list_len-i-1
    #执行交换
    list2[last_index],list2[min_index]=list2[min_index],list2[last_index]

print (list2)

#插入排序
#从列表中取出每一位，插入一个有序的新的列表里
#有序列表中从最后一位开始，和要插入的值进行两两交换，直到比较项小于插入项

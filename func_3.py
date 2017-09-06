#coding:utf-8
#无参数
#（1）列表
# print lambda : range(10)
#
# #有参数
# def a(x,y):
#     return x+y
#
# print lambda x,y:x+y
#
# #遍历列表，然后每个元素乘方,并求和
# def each_list(list1):
#     sum=0
#     for item in list1:
#         sum+=item**2
#     return sum
#
#
# #1 对于序列(seq)中item顺序迭代调用function，并且进行迭代运算（reduce）lambda x,y:x+y
# #reduce(function,seq)=》value
# #2.对于序列逐个执行函数，并做运算并返回相应结果（map）
# #map(function,seq[,seq2[,seq3....]])=》seq
# #map(func1,list1,list2,list3...)
# each_list3=lambda x,y:x*y
# print map(lambda x:x**2,range(10))
# print reduce(each_list3,map(lambda x:x**2,range(10)))
# #3.filter(function or None,seq)
# #对序列（seq）的item一次执行function(item)
# #将执行的结果为true的item组成一个list/string/tuple
# #取出列表的偶数
# foo=[2,13,512,11,53]
# print filter(lambda x:x%2==0,foo)
#
# #练习1:5！+4！+3！+2！+1！
# #1.如何上述的三个方法和匿名函数实现阶乘操作
# n=5
# reduce(lambda x,y:x*y,range(1,n+1))
# #2.求和
# print reduce(lambda x,y:x+y,[reduce(lambda x,y:x*y,range(1,i+1)) for i in range(1,n+1)])

#求100以内质数形成列表
#1.质数判断
#lambda x:not [x%i for i in range(2,x) if x%i==0]
#2.遍历100以内数，形式质数列表
print filter(lambda x:not [x%i for i in range(2,x) if x%i==0],range(2,100))



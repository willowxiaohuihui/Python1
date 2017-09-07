#coding:utf-8
#while三要素
#1.起始值   2.终止值   3.步进值
#输入一个数值，输出从0到这个数的所有奇数。
# begin=1
# end=input(u'输入一个数:')
# step=2
# list1=[]
# while begin<=end:
#     list1.append(begin)
#     begin+=step
# print (list1)

#range(begin,end+1,step)
#[begin,end+1) 实现begin<=end
end=input(u'输入一个数:')
for i in range(1,end+1,2):
    print (i,)
# end = input(u'输入一个数:')
# print (range(1,end,2))
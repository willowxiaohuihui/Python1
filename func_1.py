#coding:utf-8
#不定长参数
import func_2
#打印传入的参数
def printInfo(arg1,*vartuple):
    print u'输出'
    print arg1
    #遍历vartuple这个参数组
    for var in vartuple:
        print ','+str(var)

printInfo(10)
#10
printInfo(70,60,50)
#coding:utf-8
#输入一个星期几，输出他对应的英语名称
#1.设置一个入口，raw_input(下面条件判断，就需要判断字符串)/input（下面判断整型）
weekday=int(input(u' 请输入星期几：'))
#2.使用分支语句做星期判断
if weekday=='1':
    print ('Monday')
elif weekday=='2':
    print ('Tuesday')
elif weekday=='3':
    print ('Wes')
elif weekday=='4':
    print ('Ths')
elif weekday=='5':
    print ('Friday')
elif weekday=='6':
    print ('S')
elif weekday=='7':
    print ('Sun')
else:
    print (u' 请重新输入')


#eval()自动转换数据类型
print (eval('1+2'))
num=eval(input(u' 请输入一个数字：'))
if num%2==1:
    print (u' 你输入一个奇数')
else:
    print (u' 你输入一个偶数')

#四则运算
#1.输入三个值
first_num=eval(input(u'请输入第一个数字：'))
opa=input(u'请输入+-*/任意一个符号：')
second_num=int(input(u'请输入第二个数字：'))
#2.判断符号
if opa=='+':
    print( '%d+%d=%d'%(first_num,second_num,first_num+second_num))
elif opa=='-':
    print ('{0}-{1}={2}'.format(first_num,second_num,first_num-second_num))
elif opa=='*':
    print ('%s*%s=%s'%(first_num,second_num,first_num*second_num))
elif opa=='/':
    #3.注意除数为0
    if second_num==0:
        print (u'除数不能为零')
    else:
        print ('%s/%s=%s'%(first_num,second_num,1.0*first_num/second_num))
else:
    print (u'请非法操作')
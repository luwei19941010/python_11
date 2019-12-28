#-*-coding:utf-8-*-
# Author:Lu Wei
# func1=lambda a1,a2:a1+1
# print(func1(1,2))
#
# func1=lambda:100
# func2=lambda x1:x1*10
# func3=lambda *args,**kwargs:len(args)+len(kwargs)
#
# DATA=100
# func4=lambda a1:a1+DATA
# print(func1())
# print(func2(2))
# print(func3(1,2,3,4,k1='1',k2='3'))
# print(func4(2))
#
# DATA=100
# def fun():
#     DATA=1000
#     func5=lambda a1:a1+DATA
#     print(func5(1))
# fun()
#
# def big_num(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
#
# print(big_num(1,2))
#
# func6=lambda a,b:a if a>=b else b
# print(func6(1,2))


# USER_LIST=[]
# func1=lambda x:USER_LIST.append(x)
#
# print(func1('alex'))
# print(USER_LIST)
#
#
#
#
# func1=lambda x:x.split("l")
# print(func1('alex'))#['a','ex']

FUNC_LIST=[lambda x:x.split('l'),lambda y:y+100,lambda x,y:x+y]
print(FUNC_LIST[0]('alalala'))
print(FUNC_LIST[1](1))
print(FUNC_LIST[2](1,2))


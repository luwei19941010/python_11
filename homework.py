#-*-coding:utf-8-*-
# Author:Lu Wei
#1.列举 str、list、dict、set 中的常用方法（每种至少5个），并标注是否有返回值。
'''
str:
    strip 有返回值
    split 有返回值
    upper/lower 有返回值
    jion 有返回值
    replace 有返回值
    statswith/endswith 有返回值
    isdecimal 有返回值
    encode 有返回值
    format 有返回值
    count
list:
    append 无返回值
    insert 无返回值
    extend 无返回值
    pop    有返回值
    clear  无返回值
    remove 无返回值
    reverse 无返回值
    sort    无返回值
    count   有返回值

dict:
    update 无返回值
    get 有返回值
    keys 有返回值
    values 有返回值
    items 有返回值
    pop 有返回值

set():
    intersection 有返回值
    union 有返回值
    difference 有返回值
    add 无返回值
    discard 无返回值
    pop 有返回值随机pop

'''
#2.列举你了解的常见内置函数 【面试题】。
#其他len open id type range
#转换str int list set bool dict tuple
#数学 bin，oct，int，hex，sum,max,min,divmod,abs,float
#输入输出 input print

#3.看代码分析结果
# def func(arg):
#     return arg.replace('苍老师', '***')
#
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
#
# run()
# '''
# 执行结果
# Alex的女朋友***和大家都是好朋友
# '''


#4.看代码分析结果
# def func(arg):
#     return arg.replace('苍老师', '***')
#
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
# data = run()
# print(data)
#
# '''
# 执行结果
# Alex的女朋友***和大家都是好朋友
# None
# '''

#5.看代码分析结果
# DATA_LIST = []
#
#
# def func(arg):
#     return DATA_LIST.insert(0, arg)
#
#
# data = func('绕不死你')
# print(data)
# print(DATA_LIST)
#
# '''
# 执行结果：
# None
# ['绕不死你']
# '''



#6.
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)
#
# '''
# 你好呀
# 好你妹呀
# 你好呀
# 好你妹呀
# 你好呀
# 好你妹呀
# '''
#


#7.
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for i in range(len(func_list)):#0,1,2
#     val = func_list[i]()
#     print(val)
# '''
# 你好呀
# 好你妹呀
# 你好呀
# 好你妹呀
# 你好呀
# 好你妹呀
# '''

#8.
# tips="啦啦啦啦"
#
# def func():
#     print(tips)
#     return '好你妹呀'
#
# func_list = [func, func, func]
#
# tips='你好不好'
#
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
# '''
# 你好不好
# 好你妹呀
# 你好不好
# 好你妹呀
# 你好不好
# 好你妹呀
#
# '''

#9.
# def func():
#     return '烧饼'
#
#
# def bar():
#     return '豆饼'
#
#
# def base(a1, a2):
#     return a1() + a2()
#
#
# result = base(func, bar)
# print(result)
# '''
# 烧饼豆饼
# '''

#10.
# def func():
#     return '烧饼'
#
#
# def bar():
#     return '豆饼'
#
#
# def base(a1, a2):
#     return a1 + a2
#
#
# result = base(func(), bar())
# print(result)

# '''
# 烧饼豆饼
# '''

#11.
# v1 = lambda :100
# print(v1())
#
# v2 = lambda vals: max(vals) + min(vals)
# print(v2([11,22,33,44,55]))
#
# v3 = lambda vals: '大' if max(vals)>5 else '小'
# print(v3([1,2,3,4]))
#
# '''
# 100
# 66
# 小
# '''


#12
# def func():
#     num = 10
#     v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]#[20,110,110]
#     for item in v4:
#         print(item())
# func()
# '''
# [20,110,110]
# '''

#13.
# for item in range(10):
#     print(item)
#
# print(item)
# '''
# 0,1,2,3,4,5,6,7,8,9
# 9
# '''
#14.
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func()
#
# '''
# 9
# '''

#15

# item = '老男孩'
# def func():
#     item = 'alex'
#     def inner():
#         print(item)
#     for item in range(10):
#         pass
#     inner()
# func()
# '''
# 9
# '''



#16.
# def func():
#     for num in range(10):
#         pass
#     v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]#19,109,109
#     result1 = v4[1]()#109
#     result2 = v4[2]()#109
#     print(result1,result2)
# func()
#
#
# '''
# 109,109
# '''

#17.

# 二进制转换成十进制：v = '0b1111011'
# v = '0b1111011'
# print(int(v,base=2))
# # 十进制转换成二进制：v = 18
# v = 18
# print(bin(v))
# # 八进制转换成十进制：v = '011'
# v = '011'
# print(int(v,base=8))
# # 十进制转换成八进制：v = 30
# v=30
# print(oct(v))
# # 十六进制转换成十进制：v = '0x12
# v='0x12'
# print(int(v,base=16))
# # 十进制转换成十六进制：v = 87
# v=87
# print(hex(v))

#18.
'''
如 10.3.9.12 转换规则为二进制：
        10            00001010
         3            00000011
         9            00001001
        12            00001100
再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
'''
def ip(data):
    a=data.split('.')
    s=''
    for i in a:
        s+=bin(int(i)).lstrip('0b').zfill(8)
    print(s)
    return int(s,base=2)
print(ip('10.3.9.12'))




### day11

#### 今日内容

- 函数小高级
- lambda表达式
- 内置函数

#### 内容基本回顾：

##### 1.函数基本结构

##### 2.参数

- 形参

  - 基本参数：def func(a1,a2):pass

  - 默认值：def func(a1,a2=123):pass #注意默认值如果是不可变类型，没有问题，如果是可变类型 有问题

  - 无敌参数：*args，**kwargs

    

- 实参

  - 位置传参

  - 关键字传参

    #注意：位置传参永远在关键字传参前面

##### 3.返回值

- 默认情况返回：None
- 返回值可以返回  任意类型值。
- 特殊返回值情况：

```
def func（）
	return 1，2，3
这时返回的是元组。
```



##### 4.作用域

- 全局作用域

  

- 局部作用域

  - 优先在自己作用域中找，如果没有，则往上找父级的作用域，最终找到全局作用域

  - 子作用域只能读取或修改父级的值（可变类型的），不能进行复制

    ```
    NUM=9
    def func():#因为NUM是int 不可变类型，则不能修改
    	#如果想在函数内系修改（赋值）不可变类型的值，则需要使用global参数，直接影响全局作用域的。
    	global NUM
    	NUM=99#这时全局NUM则为99
    	#或者采用nonlocal参数，影响父级作用域。如果存在多层函数，则需要调用多层nonlocal才能影响全局作用域。
    NUM=[1,2,3]
    def func()
    	#NUM.append(99)#因为NUM是list，可变类型，则可以进行修改。NUM[1，2，3，99]
    	
    	
    ```

    

##### 5.函数嵌套

```
def func():
	name='oldboy'
	def inner():
		print(name)
	inner()
	print(name)
func()
```





### 内容详细

#### 1.函数小高级

##### 1.函数小高级

```
a=123
name='lkuwei'

def func():
	pass
v1=func  #v1() 等于func()
```

##### 2.函数名当做变量使用

```

区分
def func():
    print(123)
list_func1=[func,func,func]
list_func2=[func(),func(),func()]
print(list_func1)#func函数代码块的内存地址
print(list_func2)#func()执行了返回None
执行结果'''
123
123
123
[<function func at 0x0000000000A90A60>, <function func at 0x0000000000A90A60>, <function func at 0x0000000000A90A60>]
[None, None, None]
'''


def func():
    return 123
list_func1=[func,func,func]
list_func2=[func(),func(),func()]
print(list_func1)#func函数代码块的内存地址
print(list_func2)#func()执行了返回123

执行结果'''
[<function func at 0x0000000000770A60>, <function func at 0x0000000000770A60>, <function func at 0x0000000000770A60>]
[123, 123, 123]
'''

def func():
    return 123

info={'k1':func,'k2':func()}
print(info)
'''
{'k2': 123, 'k1': <function func at 0x0000000001130A60>}
'''

```

##### 3.函数可以当做参数进行传递

```
def func(arg)：
	print(arg)
func(1)
func([1,2,3,4])

def show ()
	return 999
func(show)
```

```
def func(arg):
    v1=arg()
    print(v1)
def show():
    print(666)

func(show)

执行结果：
666
None
```



```
def func(arg):
    v1=arg()
    print(v1)
def show():
    print(666)

result=func(show)
print(result)
执行结果：
666
None
None
```



#### 2.lambda表达式

用于表示简单的函数(只用一行代码)，并且在lambda表达式内不能定义变量。

```
#三元运算，为了解决简单的if else的情况，如：
if 1==1:
	a=123
else:
	a=456
a= 123 if 1==1 else: 456

lambda表达式，为了解决简单函数的情况，如：
def func（a1,a2):
	return a1+1
		

func1=lambda a1,a2:a1+1
```



```
func1=lambda:100
func2=lambda x1:x1*10
func3=lambda *args,**kwargs:len(args)+len(kwargs)

DATA=100
func4=lambda a1:a1+DATA
print(func1())
print(func2(2))
print(func3(1,2,3,4,k1='1',k2='3'))
print(func4(2))


DATA=100
def fun():
    DATA=1000
    func5=lambda a1:a1+DATA#因为自己没有变量，则去父级作用域里面找。
    print(func5(1))
fun()



def big_num(a,b):
    if a>=b:
        return a
    else:
        return b

print(big_num(1,2))

func6=lambda a,b:a if a>=b else b
print(func6(1,2))



```



#### 练习题

```
#一般情况下：list所有的办法基本都不会有返回值，字符串的所有方法都有返回新值。

#1.
USER_LIST=[]
func1=lambda x:USER_LIST.append(x)
print(func1('alex'))#None
print(USER_LIST)#['alex']

#2.
func1=lambda x:x.spilt("l")
print(func1('alex'))#['a','ex']
 
#3.
FUNC_LIST=[lambda x:x.split('l'),lambda y:y+100,lambda x,y:x+y]
print(FUNC_LIST[0]('alalala'))
print(FUNC_LIST[1](1))
print(FUNC_LIST[2](1,2))
```





#### 3.内置函数

- 自定义函数

- 内置函数

  - len

  - open

  - print

  - range

  - id

  - type

  - 输入输出

    - print
    - input

  - 强制转换

    - dict（）
    - list（）
    - tuple（）
    - set（）
    - int（）
    - str（）
    - bool（）

  - 数学相关

    - abs()，绝对值

      ```
      print(abs(-1))#1
      ```

    - float(),转换成浮点型（小数）

      ```
      print(float(100))#100.0
      ```

    - max()最大值

      ```
      v=[1,2,3,112,33]
      print(max(v))#112
      ```

    - min()

      ```
      v=[1,2,3,112,33]
      print(min(v))#1
      ```

    - sum()

      ```
      v=[1,2,3,112,33]
      print(sum(v))#132
      ```

    - divmod(),两个相除，得商和余数

      ```
      v=1001
      result=divmod(1001,5)
      a,b=divmod(1001,5)
      print(result)#200,1
      print(a,b)#200,1
      ```

    ```
    USER_LIST=[]
    for i in range(0,869):
        data={'name':'luwei%s'%(i,),'psd':'xyz%s'%(i,)}
        USER_LIST.append(data)
    
    LIST_len=len(USER_LIST)
    PEER_LINE=10
    PAPG_NUM,a=divmod(LIST_len,PEER_LINE)
    if a>0:
        PAPG_NUM+=1
    
    while True:
        USER_PAPG=int(input('PAPG NUM：'))
    
        if USER_PAPG<=0 or USER_PAPG>PAPG_NUM:
            print('again')
        else:
                start_line=(USER_PAPG-1)*10
                end_line=USER_PAPG*10
                for i in USER_LIST[start_line:end_line]:
                    print(i)
    ```

    

    - bin() 十进制转二进制

    ```
    a=0b1001  #可以直接转8 10 16 进制
    print(type(a))###注意这是a是int类型也就是为十进制
    
    a=10
    print(bin(a))#0b1010
    print(type(bin(a)))#<class 'str'>
    
    ```

    - oct()十进制转八进制

    ```
    a=0o11 #可以直接转2 10 16 进制
    print(type(a))###注意这是a是int类型也就是为十进制
    
    a=10
    print(oct(a))#0o12
    print(type(bin(a)))#<class 'str'>
    ```

    - int()转十进制

    ```
    #2进制转十进制
    a=0b1010
    print(int(a))#10
    a='0b1010'
    print(int(a,base=2))
    
    #8进制转十进制
    a=0o12
    print(int(a))#10
    a='0o12'
    print(int(a,base=8))
    
    #16进制转十进制
    a=0xa
    print(int(a))#10
    a='0xa'
    print(int(a,base=16))
    ```

    

    - hex()十进制转十六进制

    ```
    a=0x9  #可以直接转2 8 10 进制
    print(type(a))###注意这是a是int类型也就是为十进制
    
    a=10
    print(oct(a))#0xa
    print(type(bin(a)))#<class 'str'>
    ```

    

  练习题

  ```
  #1.将ip='192.168.1.2',转化为二进制
  ip_new_list=[]
  ip='192.168.1.2'
  ip_list=ip.split('.')
  for i in ip_list:
      i_2=bin(int(i))
      ip_new_list.append(i_2)
  
  ip_0b='.'.join(ip_new_list)
  print(ip_0b)#0b11000000.0b10101000.0b1.0b10
  
  
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
  ```

  ![image-20191228163709253](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191228163709253.png)

  


















































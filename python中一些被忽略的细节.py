# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:36:13 2018

@author: Administrator
"""

# =============================================================================
# 全局变量：Python的全局变量并不是程序级别的（即全局唯一），而是模块级别的。
# =============================================================================
import sys
import test

a = 1

def func1():
    global a
    a += 1

def func2():
    test.a += 1

def func3():
    module = sys.modules['test']
    module.a += 1

func1()
func2()
print(test.a)

func3()
print(test.a)

# =============================================================================
# Python中的else:Python语法中比其他语言多了两个else
# =============================================================================
while True:
    # 正常执行的语句 ....
else:
    # while语句正常结束的时候执行，出现异常则不执行
# 进阶1：如果while循环里面遇到了break语句，else语句会执行吗？ 不会因为循环没有正常结束
# 进阶2：如果while循环最后，遇到了continue语句，else语句还会执行吗？ 会，因为循环会继续执行到结束
# 进阶3：如果while循环内部出现异常，else语句还会执行吗？    不会
i=1
while i < 10 :  
    print(i)   
    i = i + 1   
    if i == 7:  
        break;  
else:  
    print('It is over')  

i = 0  
while i < 10 :       
    i = i + 1   
    if i == 4:  
        pass  
    if i == 6:  
        continue  
    print(i)   
else:  
    print('It is over.') 

  
try:
    # 正常执行的语句
except:
    # 出现异常时执行的语句
else:
    # 没有出现异常，就执行else里面的语句 
finally:
    # 无论是否出现异常，都要执行finally语句     


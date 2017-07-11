# coding=utf-8
'''斐波那契数列
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
'''
'''
首先祝贺自己把这道题高出来
这道题有两个难点
1是想清楚a，b，c三个数如何一起循环，而且是每三个一循环
2是想清楚如何构建整体的框架。。
最后是要测试。。。边测试变修改才是最完善的。。。
'''
n = int(raw_input('你想要第几个数？：'))
i = 2
a = 0
b = 1
if n > 2:
    while i < n:
        c = a + b
        a = b + c
        b = c + a
        i = i + 3
    if n % 3 == 0:
        print c
    elif n % 3 == 1:
        print a
    elif n % 3 == 2:
        print b
elif n == 2:
    print '1'
else:
    print '0'

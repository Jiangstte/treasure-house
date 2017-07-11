# -_- coding= utf-8 -_-

'''
a = (1, 2, 3, 4, 5)
c = ''
for b in range(0, 4):
    c = c + str(a[b])
print int(c)
'''

'''
这两个程序的唯一区别就是c的定义值一个在里面，一个在外面。但是结果是完全不同的。在里面的每次外部的for循环要重新转一圈时，c的值被重新定义成了空的然后再来进行后面操作。。而第一个是在外面，则每次外部循环进行一个
循环时，c的值并没有被清空，而是在原来的基础上继续往上累加，所以会出现金字塔型的数据分布！！！以后一定要切记定义变量位置应该在何处定义！！！
'''

'''
from itertools import permutations
c = ''
for a in permutations([1, 2, 3, 4], 3):
    for b in range(0, len(a)):
        c = c + str(a[b])
    print (int(c))


from itertools import permutations

for i in permutations([1, 2, 3, 4], 3):
    k = ''
    for j in range(0, len(i)):
        k = k + str(i[j])
    print (int(k))
'''
'''
from itertools import permutations
for i in permutations([1, 2, 3, 4], 3):
    print i
'''
'''
这个事ls7用的副本。。。
a = 0
b = 1
c = a + b
b = a + c
a = b + c
c = a + b
b = a + c
a = b + c
print a, b, c
'''

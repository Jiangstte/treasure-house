# -_- coding= utf-8 -_-
# 你自己看吧，这是关于在1，2，3，4几个数字中随机抽取三个数字组成字串的几种想法，主要的就是2种方法，一种添加法，一种直接书写法
'''
c = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (k != i):
                c.append([i, j, k])

d = len(c)
print d
'''

'''
a = [1, 2, 3, 4]
list = [i * 100 + j * 10 +
        k for i in a for j in a for k in a if (i != j) and (j != k) and (k != i)]

list.sort()
print list[0], list[-1]
b = len(list)
print b
'''

'''
a = []
b = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            a.append(i * 100 + j * 10 + k)
            if i == j == k:
                b.append(i * 100 + j * 10 + k)
print a
print b
'''

'''
a = [1, 2, 3, 4]
b = [i * 100 + j * 10 + k for i in a for j in a for k in a if i != j != k]
print b
'''

from itertools import permutations

for i in permutations([1, 2, 3, 4], 3):
    k = ''
    for j in range(0, len(i)):
        k = k + str(i[j])
    print (int(k))

# coding= utf-8
'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''

x = int(raw_input('请输入第一个数:'))
y = int(raw_input('请输入第二个数:'))
z = int(raw_input('请输入第三个数:'))

'''
这个程序其实很简单，最重要的就是你需要把每一种情况想全面了就好了
然后要记得测试，出现问题一看你就知道了
第二种方法是使用列表，然后使用排序的方法将他排序就好了
'''
'''
if x > y:
    a = x
    x = y
    y = a
    if y > z:
        b = y
        y = z
        z = b
        if x > z:
            c = x
            x = z
            z = c
            print x, y, z
        elif x > y:
            e = x
            x = y
            y = e
            print x, y, z
        else:
            print x, y, z
    elif x > z:
        d = x
        x = z
        z = d
        print x, y, z
    else:
        print x, y, z
elif y > z:
    b = y
    y = z
    z = b
    if x > z:
        c = x
        x = z
        z = c
        print x, y, z
    else:
        print x, y, z
elif x > z:
    d = x
    x = z
    z = d
    print x, y, z
else:
    print x, y, z
'''

'''
a = [x, y, z]
a.sort()
print a
'''

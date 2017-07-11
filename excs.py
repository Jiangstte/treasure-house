#coding= utf-8

def jia(a,b):
    print"做个加法嘛:%s + %s" % (a,b)
    return a + b

def jian(a,b):
    print"做个减法嘛:%s - %s" % (a,b)
    return a - b

def cheng(a,b):
    print"做个乘法嘛:%s * %s" % (a,b)
    return a * b

def chu(a,b):
    print"来个除法试试:%s / %s" % (a,b)
    return a / b

q = jia(1,2)
w = jian(2,1)
e = cheng(2,2)
r = chu(4,2)

print "这些东西的结果是什么东西啊：%s,%s,%s,%s" % (q,w,e,r)

print "让我试一下这个东西可以算不：3*5-2*2?"
o = jian(cheng(3,5),cheng(2,2))
print "这就是最终的结果：%s" % o

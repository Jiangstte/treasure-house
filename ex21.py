def cpy_yici(a,b):
    print "ADDING %s + %s " % (a,b)
    return a + b

def cpy_erci(a,b):
    print "SUBTRACTING %s - %s " % (a,b)
    return a - b

def cpy_sanci(a,b):
    print "wo guan ni shen me dong xi %s * %s " % (a,b)
    return a * b

def cpy_sici(a,b):
    print "you ben shi ni lai yao wo a %s / %s " % (a,b)
    return a / b

print "na wo men lai gao shi qing ba !"

age = cpy_yici(20,5)
height = cpy_erci(183,5)
weight = cpy_sanci(77,2)
iq = cpy_sici(500,2)

print "nianling:%s,shengao:%s,zhongliang:%s,zhishang:%s" % \
(age,height,weight,iq)

print "here is a puzzle"

what = cpy_yici(age,cpy_erci(height,cpy_sanci(weight,cpy_sici\
(iq,2))))

print "that because:",what,"can you do yt by hand?"


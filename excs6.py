i = 0
num = []
cpy = ">"
yuyanjia = int(raw_input("now please input a number:\n %s " % cpy))
nvwu = int(raw_input("now choose a step to jump:\n %s " % cpy))

while i < yuyanjia:
    print "now the number is %s" % i
    num.append(i)

    i += nvwu
    print "now the number is %s" % i
    print num

print "the number is:" ,num

for i in num:
    print "now the number in num is :%s" % i

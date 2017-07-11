i = 0
number = []

while i < 6:
    print "at the top i is %s" % i
    number.append(i)

    i += 1
    print "numbers now:",number
    print "at the bottom i is %s " % i

print "the numbers:"

for num in number:
    print num


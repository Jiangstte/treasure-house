people = 30
cars = 40
trucks = 15


if cars > people and cars > trucks:
    print "We should take the cars."
elif cars < people or people > trucks:
    print "We should not take the cars."
else:
    print "We can't decide."

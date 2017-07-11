from sys import argv

script,user_name,user_age = argv
easy = '> '

print "Hi %s,you are %s year old,I'm the %s script." % (user_name,user_age,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(easy)

print "Where do you live %s?" % user_name
lives = raw_input(easy)

print "What kind of comuter do you have?"
computer = raw_input(easy)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes,lives,computer)

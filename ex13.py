from sys import argv

script,first,second,third = argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third

forth = raw_input ("Why do you like it?")
fifth = raw_input ("I don't know what it's? ")
 
sixth = raw_input ("you need input a number:")

print "so you like %r,you don't know %r ,and the number is %r." % (forth,fifth,sixth)



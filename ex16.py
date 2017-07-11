from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C (^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
txt = open(filename, 'w')

print "Truncating the file. Goodbye!"
txt.truncate()

print "Now I'm going to ask you foe three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write there to the file."

str = (line1,"\n",line2,"\n",line3,"\n")
txt.writelines(str)

print "And finally, we close it."
txt.close()

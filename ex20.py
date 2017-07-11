from sys import argv

script,input_file = argv

def cpy_yici(f):
    print f.read()

def cpy_erci(f):
    f.seek(0)

def cpy_sanci(line_count,f):
    print line_count, f.readline(),

yuyanjia = open(input_file)

print "first let's print the whole file:\n"

cpy_yici(yuyanjia)

print "now let's rewind,kind of like a tape."

cpy_erci(yuyanjia)

print "let's print three lines:"

nvwu = 1
cpy_sanci(nvwu,yuyanjia)

nvwu = nvwu + 1
cpy_sanci(nvwu,yuyanjia)

nvwu = nvwu + 1
cpy_sanci(nvwu,yuyanjia)


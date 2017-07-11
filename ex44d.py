class Other(object):
 
    def diyige(self):
	print "zhe shi di yi ge de "

    def dierge(self):
	print "zhe shi di er ge de "

    def disange(self):
	print "zhe shi di san ge de "

class Child(object):

    def __init__(self):
	self.other = Other()

    def dierge(self):
	self.other.dierge()

    def diyige(self):
	print "CHILD,diyige()"

    def disange(self):
	print "CHILD,BEFORE OTHER disange()"
	self.other.disange()
	print "CHILD,AFTER OTHER disange()"

son = Child()

son.dierge()
son.diyige()
son.disange()


class yuyanjia(object):

    def jinshui(self):
	print "zuo wan yan de shi jin shui"

class pingmin(yuyanjia):

    def jinshui(self):
	print "zuo wan yan de shi cha sha "

dad = yuyanjia()
son = pingmin()

dad.jinshui()
son.jinshui()

class yuyanjia(object):

    def jinshui(self):
	print "zuo wan yan de shi ge jin shui"

class pingmin(yuyanjia):

    def jinshui(self):
	print "zuo wan yan de shi ge cha sha"
        super(pingmin,self).jinshui()
	print "wo ye bu zhi dao zuo wan yan de shi ge sha"

dad = yuyanjia()
son = pingmin()

dad.jinshui()
son.jinshui()

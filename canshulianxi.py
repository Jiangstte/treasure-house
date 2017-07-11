#coding= utf-8
def story(**kwds):  # 定义了一个story的函数，参数的个数给定义，但是输出是字典
    # 返回这样的一句话，采用提供的两个参数
    return 'Once upon a time,there was a %(job)s called %(name)s.' % kwds


def power(x, y, *other):  # 定义了这样的一个函数，参数有x，y，还有其他。。
    if other:  # 如果other 这些参数
        print 'Received redundant parameters:', other  # 打印这样的一句话，还有 other
    return pow(x, y)  # 返回这样的x，y的pow函数


def interval(start, stop=None, step=1):  # 定义了一个函数，一个位置参数，两个默认参数
    'Imitates range() for step > 0'  # 是个解释，解释下面这段代码是在模仿给定一个范围，然后step逐步达到的一个过程
    if stop is None:  # 如果stop这个参数没有被设置，采用的是默认参数
        start, stop = 0, start  # 那么start参数赋值为0，，stop参数赋值位置参数原来的值
    result = []  # result定义了一个列表
    i = start  # 参数i赋值了start
    while i < stop:  # 当参数i小于stop时
        result.append(i)  # 在result中添加i元素
        i += step  # i在原有的基础上加上步数
    return result  # 输出结果

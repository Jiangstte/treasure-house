# ```___```  coding= utf-8  `````_____````````
'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''

'''
这道题很简单，，按照数学知识写出循环就好了。我觉得没有必要按照他们代码那样写。太麻烦，让别人看不懂都。
'''
a = raw_input("请输入你的月利润(万元)：")
i = int(a)
if i <= 10:
    M = i * 0.1
elif 10 < i <= 20:
    M = 10 * 0.1 + (i - 10) * 0.075
elif 20 < i <= 40:
    M = 10 * 0.1 + 20 * 0.075 + (i - 20) * 0.05
elif 40 < i <= 60:
    M = 10 * 0.1 + 20 * 0.075 + 20 * 0.05 + (i - 40) * 0.03
elif 60 < i <= 100:
    M = 10 * 0.1 + 20 * 0.075 + 20 * 0.05 + 20 * 0.03 + (i - 60) * 0.015
else:
    M = 10 * 0.1 + 20 * 0.075 + 20 * 0.05 + \
        20 * 0.03 + 40 * 0.015 + (i - 100) * 0.01
print M + i
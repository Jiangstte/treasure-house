#___---___ coding= utf-8
'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

'''
1.定义一个字典，将得到的月份与之比较，输出之前一共有多少天
2.再将给的天数加上
3.再判断是不是闰年，然后加1
'''

'''
这道题的感悟是要明确数据类型，raw_input输入的字符串。而你又希望他是数据，能够直接做比较
所以你需要在其前面加上int来改变数据类型。而后面字典的键时用的是字符串，所以你不用将他再转换格式了
'''
n = int(raw_input("请输入年份："))
y = raw_input("请输入月份：")
r = int(raw_input("请输入日期："))

a = {'1': "0", '2': "31", '3': "59", '4': "90", '5': "120", '6': "151", '7': "181",
     '8': "212", '9': "242", '10': "273", '11': "304", '12': "334", }
i = 0
if n % 4 == 0 or (n % 400 == 0 and n % 100 != 0):
    i += 1
print int(a[y]) + r + i

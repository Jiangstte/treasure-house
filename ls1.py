import random
import string


def rand_str(num, len=7):
    f = open('file.txt', 'w')
    count = 1
    for i in range(num):
        restr = ''
        chars = string.ascii_lowercase + string.digits
        for i in range(len):
            restr += random.choice(chars)

        f.write(str(count) + '' + restr + '\n')
        count += 1

    f.close


if __name__ == '__main__':

    rand_str(200, 20)

import random


str = '1234567890abcdefghijklmnopqrstuvwsyz'
for i in range(10):
    res = random.sample(str, 8)
    if not res[0].isdigit():
        print(''.join(res) + '@163.com')
    else:
        res[0] = random.choice('abcdefghijklmnopqrstuvwsyz')
        print(''.join(res) + '@163.com')

# Filename:001.py
import math
import datetime
import time

cnt = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
             if i != j and j != k:
                 print(i*100+j*10+k)
                 cnt += 1
print(cnt)


# Filename: 002.py
i = int(input('Enter the profit:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
   if i > arr[idx]:
        r += (i-arr[idx])*rat[idx]
        # print((i-arr[idx])*rat[idx])
        # i = arr[idx]
print(r)

# -*- coding:utf-8 -*-
# Filename: 03.py


num = 1
count = 0
while True:
    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:
        count += 1
        print(num)
        if count>= 2:
            break

    num += 1
# -*- coding:utf-8 -*-
# Filename: 04.py

dtstr = str(input('Enter the datetime:(20151215):'))
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr = dtstr[:4] + '0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print(int((dt-another_dt).days) + 1)


# -*- coding: utf-8 -*-
import re

with open("input_2.txt", 'r') as input1:
    lines = input1.readlines()

q = re.compile('''(\d+)-(\d+)\s+(\w):\s*(\w+)''')

cn = 0
for y in (lines):
    z = q.match(y)
    if (z is not None):
        a = int(z.group(1))
        b = int(z.group(2))
        c= z.group(3)
        f = z.group(4).count(c)
        if(f>=a and f<=b):
            cn +=1

cn2 = 0
for y in (lines):
    z = q.match(y)
    if (z is not None):
        a = int(z.group(1))
        b = int(z.group(2))
        c= z.group(3)
        f = z.group(4)
        if(f[a-1]==c and f[b-1]!=c):
            cn2 +=1
        elif(f[a-1]!=c and f[b-1]==c):
            cn2 +=1
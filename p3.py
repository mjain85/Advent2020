# -*- coding: utf-8 -*-
import numpy as np
from functools import reduce

with open("input_3.txt", 'r') as input1:
    lines = input1.readlines()

z = np.zeros((len(lines),len(lines[0].strip())))

for i,l in enumerate(lines):
    for j,v in enumerate(l.strip()):
        if(v=='#'):
            z[i,j]=1

d = [(1,1), (3,1), (5,1),(7,1),(1,2)]
#right, down
totalTree = []

for vr,vd in d:
    k = 0
    tree = 0
    for i in range(vd,z.shape[0], vd):
        k = k+vr
        k = k % z.shape[1]
        if(z[i,k]==1):
            tree +=1
    totalTree.append(tree)
print(reduce(lambda a,b:a*b, totalTree))

    
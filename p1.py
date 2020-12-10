# -*- coding: utf-8 -*-

with open("input_1.txt", 'r') as input1:
    lines = input1.readlines()
    nums = []
    for l in lines:
        nums.append(l)

nums = sorted([int(n) for n in nums])

def findTwoSum(nums, kSum):
    i = 0
    j = len(nums)-1
    while(i<j):
        s = nums[i]+nums[j]
        if(s>kSum):
            j = j-1
        elif(s<kSum):
            i = i+1
        if(s==kSum):
            print(i,j)
            return (i,j)
            break
    return (-1,-1)

kSum = 2020

def findThreeSum(nums, kSum, p):
    i = 0
    j = len(nums)-1
    while(i<j):
        s = nums[i]+nums[j]
        if(s>kSum):
            j = j-1
        elif(s<kSum):
            i = i+1
        if(s==kSum):
            print(i,j)
            return (i,j)
            break
        if(j==p):
            j=j-1
        if(i==p):
            i+=1
    return (-1,-1)

for n in range(len(nums)):
    i,j = findThreeSum(nums, kSum-nums[n], n)
    if(i!=-1 and j !=-1):
        print(n,i,j)
        break
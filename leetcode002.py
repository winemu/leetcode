#!/usr/bin/python

"""
leetcode002.py
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
==============
 Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
l1=[2,4,3]
l2=[5,6,4]
l3=[]

def ltoi(l):
    i=0
    j=1
    ret=0
    n=len(l)
    while(i<n):
        ret=(l[i])*j+ret
        i=i+1
        j=j*10
    return(ret)

def addTwoNumbers(l1,l2):
    l=[]
    k=ltoi(l1)+ltoi(l2)
    while(k>0):
        l.append(k%10)
        k=k//10
    return(l)


l3=addTwoNumbers(l1,l2)
print(l3)




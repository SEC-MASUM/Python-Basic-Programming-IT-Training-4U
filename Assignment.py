#NO-1
"""
def reverslist(List):
    list_len = len(List)
    if list_len == 1:
        return List
    return [List[-1]] + reverslist(List[:-1])

list = [2, 3, 4, 5, 6, 7]
print reverslist(list)
"""

#NO-2
"""
n = int(raw_input("Enter a Number: "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i

print factorial
"""

#No-3
"""
def TowerHanoi(n, start, middle, end):

    if n>=1:
        TowerHanoi(n-1, start, end, middle)
        print "Move From %s-->%s"%(start,end)
        TowerHanoi(n-1, middle, start, end)


num_of_disk = int(raw_input("Enter the number of disk: "))
start = raw_input("Enter the Start Point: ")
end = raw_input("Enter the ending Point: ")
Middle = raw_input("Enter the Middle Point: ")

TowerHanoi(num_of_disk, start, Middle, end)
"""


#NO-4
"""
num = int(raw_input("Enter a Number: "))
dictionary = {}
for i in range(1,num+1):
    dictionary[i] = i*i

print "Print the Output: ",dictionary
"""

#No-5
"""
from collections import deque
queue = deque("123456789")
print "Printed Main Queue: ",queue

queue.append("0")
print "Printed After append '0' :",queue

queue.popleft()
print "Printer after Pop from Left: ",queue

queue.append("Number")
print "Printed After append a 'Number'",queue

queue.pop()
print "Printed After Pop from Right:",queue
"""

#No-6
"""
input = raw_input()
list = input.split(',')
tuple = tuple(list)
print list
print tuple
"""

#No-7
"""
def BinarySearch(list, key):
    start = 0
    end=len(list)-1
    index = -1
    while start <= end and index== -1:
        mid =int((start + end)/2)
        if list[mid] == key:
           index = mid
        elif list[mid] > key:
            end = mid-1
        else:
            start = mid+1


    if start > end:
        print "Faild"

    return index

print "Enter the numbers in increasing order"

List = [int(x) for x in raw_input().split()]
print List
Key = int(raw_input("Enter your wanted element: "))
print BinarySearch(List, Key)
"""

#No-8
"""
def withoutDuplicate(list):
    new_list = []
    temp = set()
    for element in list:
        if element not in temp:
            temp.add(element)
            new_list.append(element)

    new_list.reverse()
    return new_list


List = [12,24,35,24,88,120,155,88,120,155]
print withoutDuplicate(List)
"""

#No=9
"""
def num_of_cknANDrbt(head,leg):
    i=0
    for ckn in range(head+1):
        rbt=head-ckn
        if 2*ckn+4*rbt == leg:
            i=1
            print ckn,rbt

    if i==0:
        print "No solution"

Head = int(raw_input("Enter Number Of Heads: "))
Leg = int(raw_input("Enter Number of Legs: "))
print "Number of chickens and rabbits:"
num_of_cknANDrbt(Head,Leg)
"""


#No-10
"""
import math
C, H = 50, 30
result = []
input = [int(x) for x in raw_input().split(',')]
for D in input:
    result.append(str(int(math.sqrt((2 * C * D) / H))))

print ','.join(result)
"""

#No-11
"""
input_dim = [int(x) for x in raw_input().split(',')]
x = input_dim[0]
y = input_dim[1]
matrix = [[0 for col in range(y)] for row in range(x)]
for i in range(x):
    for j in range(y):
        matrix[i][j] = i*j

print matrix
"""

#No-12
"""
input = [x for x in raw_input().split(',')]
input.sort()
print ','.join(input)
"""

#No-13
"""
input = [x for x in raw_input().split(' ')]
without_duplicate = set(input)
print ' '.join(sorted(without_duplicate))
"""

#No-14


#No-15
"""
import random
print random.uniform(5,95)
"""




'''Write code to find max.m bet.n n numbers, n varies from 10,100 and 10000'''
n = int(input('Enter Total numbers'))
print('Enter', n,'numbers')
cur_max=int(input())

for i in range(n-1):
    x=int(input())
    if cur_max<x:
        cur_max=x


print('the maximum number is', cur_max)
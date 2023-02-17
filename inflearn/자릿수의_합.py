import sys


def digit_sum(x):
    return sum(x)
    

sys.stdin=open(r"C:\Users\junga\Desktop\coding\git\nature\inflearn\자릿수의_합.txt","rt")

n=map(int,input())
data=list(map(int,input().split()))


max=0
max_num=0

for number in data:
    temp=digit_sum(list(map(int,str(number))))

    
    if temp < max :
        continue
    elif temp > max:
        max=temp
        max_num=number
    
print(max_num)

import sys
sys.stdin=open(r"C:\Users\junga\Desktop\coding\git\nature\inflearn\k번째수_input.txt","rt")

T=int(input()) # number of Test Case
for i in range(T):
    n,s,e,k=map(int,sys.stdin.readline().split())
    data=list(map(int,sys.stdin.readline().split()))
    result=data[s-1:e]
    result.sort()
    print('#{} {}'.format(i+1,result[k-1]))

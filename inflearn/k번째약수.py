# from selectors import EpollSelector
import sys
sys.stdin=open(r"C:\Users\junga\Desktop\coding\git\nature\inflearn\input.txt","rt")

n,k=map(int,input().split())
#6,3
if (n%2) ==0:
    cnt=(n//2) -1
else:
    cnt=n//2

#약수구하기(초반부)
divisor=[]
for i in range(1,cnt+1):
    if n%i==0:
        divisor.append(i)

final=[]
# 최종 값 출력
if len(divisor)>=k:
    print(divisor[k-1])
else: #후반에 있으면 전반부를 이용하여 후반부 약수구하기 
    # final=[]
    for i in divisor:
        final.append(n//i)
    final.extend(divisor)
    result=list(set(final))
    result.sort()
    if len(result)<k:
        print(-1)
    else:
        print(result[k-1])

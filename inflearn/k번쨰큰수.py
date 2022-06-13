import sys
sys.stdin=open(r"C:\Users\junga\Desktop\coding\git\nature\inflearn\k번째큰수_input.txt","rt")

n,k=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

#모든 조합 합계 구한 후, 보기
result=set()
for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        for l in range(j+1,len(data)):
            result.add(data[i]+data[j]+data[l])

result=list(result)
result.sort(reverse=True)
print(result[k-1])


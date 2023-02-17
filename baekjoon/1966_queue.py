import sys
# sys.stdin=open(r"C:\Users\junga\Desktop\coding\git\nature\baekjoon\input.txt","rt")
# test3=

T=int(sys.stdin.readline())
for _ in range(T):
    n,k=map(int,input().split())
    data=list(map(int,sys.stdin.readline().split()))

    point=0
    order=1
    print_queue=[]
    priority=max(data)
    while 1:
        if (priority==data[point]):
            if point==k: 
                break
            else:
                data[point]=-1
                priority=max(data)
                order+=1
                
        point=(point+1)%len(data)


    print(order)
    

    
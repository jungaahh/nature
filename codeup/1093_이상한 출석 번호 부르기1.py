n=input()
s=list(map(int,input().split()))
print(s)

stu_list = list(range(1,24))

for i in range(0,23):
    stu_list[i]=s.count(i+1)
    print(stu_list[i], end=' ')
import sys

sys.stdin=open(r"C:\Users\junga\Desktop\coding\git\nature\inflearn\대표값_input.txt","rt")
n=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))


avg=round((sum(data)/len(data))) #리스트 평균

diff=[]
least=data[0]-avg
student_id=1

for i in range(0,len(data)):   
    #diff.append(point-avg)
    if abs(data[i]-avg) > abs(least) :
        continue
    elif abs(data[i]-avg) < abs(least) :
        student_id=i+1
        least= data[i]-avg
    elif ( abs(data[i]-avg) == abs(least)) & ((data[i]-avg) > least) :
        student_id=i+1
        least= data[i]-avg

        
print('{} {}'.format(avg,student_id))


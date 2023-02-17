import sys

def check_all_clean(now_map,direction):
    for x,y in direction:
        if room[now_map[1]+x][now_map[0]+y]==0:
            return False
    return True
    
# sys.stdin=open(r'C:\Users\junga\Desktop\coding\git\nature\baekjoon\14503.txt','rt')

#방 사이즈 입력
N,M=map(int,input().split()) # 세로,가로
r,c,d=map(int,input().split()) # 초기위치 선언

#룸 현황 입력
room=[]
cnt=0
for _ in range(0,N):

    room.append(list(map(int,input().split())))


# 방향 별 이동경로 선언
turn_left=[(0,-1),(-1,0),(0,1),(1,0)] #왼쪽으로 돌 때
straight=[(-1,0),(0,1),(1,0),(0,-1)] #후진 시 사용

##청소로직
while 1 :
    if room[r][c]==0: 
        room[r][c]=1
        cnt+=1
        print(cnt,r,c)

    # 네 방향 모두 청소가 되고,벽이면 작동을 멈춤
    if check_all_clean([c,r],straight):
        x,y=straight[(d+2)%4]
        if ((r+x)==0) | ((r+x)==(N-1)) | ((c+y)==0) | ((c+y)==(M-1)): #벽조건
            break
        else:
            r=r+x
            c=c+y

    #is_clean=0
    for _ in range(0,len(turn_left)):
        left_x,left_y=turn_left[d]
        d=(d-1)%4
        if room[r+left_x][c+left_y]==0:
            r=r+left_x
            c=c+left_y
            # is_clean=1
            break
    # if is_clean==1:
    #     break



print(cnt)
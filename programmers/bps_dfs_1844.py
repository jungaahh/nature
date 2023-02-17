from collections import deque

# 초기작성, 런타임 에러...
def solution(maps):
    answer = 0
    m=len(maps[0])
    n=len(maps)

    #방문노드
    visited_node= [[False for col in range(len(maps[0]))] for row in range(len(maps))]
    #방문예정노드. 초기값은 첫번째 위치 조정
    needed_node=deque()
    needed_node.append([0,0])

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    # DFS 이용
    while needed_node:
        x,y=needed_node.popleft()
       
        
        # 탐색 시작
        #visited_node.append([x,y]) 
        visited_node[x][y]=True
        if [x,y]==[n-1,m-1]:
            return maps[x][y]
            break # 종료조건, 마지막도착지점까지 가면 완료
        
        for (temp_x,temp_y) in zip(dx,dy):
            new_x=x+temp_x
            new_y=y+temp_y
             # 맵의 범위조건 추가
            if new_x<0 or new_y<0 or new_x>=n or new_y>=m:
                continue
            # 이미 방문한 노드 조건 추가
            if visited_node[new_x][new_y] :
                continue
            if maps[new_x][new_y]==1:
                maps[new_x][new_y]=maps[x][y]+1
                needed_node.append([new_x,new_y])
          
            

    return -1


if __name__=="__main__":
    maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
 #   maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    answer=solution(maps)
    print(answer)

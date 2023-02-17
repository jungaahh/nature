# 흔히 수학에서 사용하는 X축이 col, Y측이 row 개념


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = -1
    # 1. 테두리 구하기
    #  - 가로*세로 이차원 배열 선언
    # 1.1 면적단위로 모두 True 입력 
    rec_maps=[[0 for i in range(102)] for j in range(102)] #100까지 있지만 경로탐색하는 범위까지 생각하여 +1의 버퍼를 둬야 함
        #모서리가 겹치는 경우, 다른경우가 있으므로 2배 늘려서 측정해야 함
    for rec in rectangle:
        for i in range(rec[0]*2,rec[2]*2+1):
            rec_maps[i][rec[1]*2:rec[3]*2+1]=[1 for j in range(rec[1]*2,rec[3]*2+1)]

    # # 1.2 최종 경로 테두리를 제외하고는 False입력
    temp=[]
    for i in range(1,len(rec_maps)-1): 
        for j in range(1,len(rec_maps[i])-1):
            if rec_maps[i-1][j] and rec_maps[i+1][j] and rec_maps[i][j-1] and rec_maps[i][j+1]:
               # 겹치는 모서리인 경우, 0으로 되어 경로가 끊기므로 이들은 테두리로 남겨야 함
                if rec_maps[i-1][j] and rec_maps[i][j-1] and rec_maps[i-1][j-1]==0 :
                    continue
                elif rec_maps[i+1][j] and rec_maps[i][j-1] and rec_maps[i+1][j-1]==0 :
                    continue
                elif rec_maps[i-1][j] and rec_maps[i][j+1] and rec_maps[i-1][j+1]==0 :
                    continue
                elif rec_maps[i+1][j] and rec_maps[i][j+1] and rec_maps[i+1][j+1]==0 :
                    continue
                else:
                    temp.append([i,j])
        
    for i,j in temp:
        rec_maps[i][j]=0

    # BFS시연

    needed_node=list()
    needed_node.append([characterX*2,characterY*2,1])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while needed_node:
        x,y,d=needed_node.pop(0)
        if rec_maps[x][y]>1:
            continue
        if x==(itemX*2) and y==(itemY*2):
            return (d-1)//2

        else:
            rec_maps[x][y]+=d
            for temp_x,temp_y in zip(dx,dy):
                if rec_maps[x+temp_x][y+temp_y]==1:
                    needed_node.append([x+temp_x,y+temp_y,d+1])


    return answer

    

    # 맨 겉의 테두리 외에는 False로 변경

if __name__=="__main__":
    rectangle=[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
    characterX,	characterY	=9,7
    itemX,	itemY=6,1
    # result=17


    answer=solution(rectangle,characterX,characterY,itemX,itemY)
    print(answer)
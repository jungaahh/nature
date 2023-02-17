from heapq import heappop,heappush


def solution(jobs):
    answer=0
    init=0
  

    h=[]
    for job in jobs:
        heappush(h,(job[0],job[1]))
        init+=job[0]
    

    # 시작시간이 지나면 모두 새로운 시작시간으로 update, 우선순위는 작업시간이 짧은시간으로
    
    while len(h)>0:
        start,time=heappop(h)
        answer+=(start+time)
   #     print(answer,start,time)
    #    print(h)
        temp_h=[]
        while 1:
            if len(h)>0:
                if h[0][0]<=(start+time):
                    a,b=heappop(h)
                    # wait+=(a-init)
                    heappush(temp_h,b)
                else: #시작시간이 지나지 않으면 break-=
                    break
            else : 
                break

       
        for temp in temp_h:
            heappush(h,(start+time,temp))

    
    return (answer-init)//len(jobs)

if __name__=="__main__":
    jobs=[[1,4],[7,9],[1000,3]]
    print(solution(jobs))


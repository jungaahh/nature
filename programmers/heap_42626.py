from heapq import heapify,heappush,heappop
#heap 사용

def solution(scoville, K):
    
    #스코빌지수 입력
    heapify(scoville)
   # print(scoville)

    if (scoville[0]==0) & (scoville[1]==0) :
        return -1
    cnt=0
    while (scoville[0]<K):
        if len(scoville)<2:
            return -1
        cnt+=1
        min=heappop(scoville)
        #print(heap.heap_array)
        min_2nd=heappop(scoville)
        score=min+(min_2nd*2)
        heappush(scoville,score)
    return cnt

if __name__=="__main__":
    scoville=[0,1]
    K=7
    answer=solution(scoville,K)


    example=[10,8,6,3,1]
    print(example)
    heapify(example)
    print(example)
    heappush(example,0)
    print(example)
    min=heappop(example)
    print(example)

    print(answer)

class Heap:
    def __init__(self):
        self.heap_array=list()
        self.heap_array.append(None)
        # self.heap_array.append(data)

    def move_up(self,inserted_index):
        parent=inserted_index//2
        if parent<1:
            return False
        if self.heap_array[parent]>self.heap_array[inserted_index]:
            self.heap_array[parent],self.heap_array[inserted_index]=self.heap_array[inserted_index],self.heap_array[parent]
            return True
        else:
            return False



    def insert(self,data):
        if len(self.heap_array)<=1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_index=len(self.heap_array)-1
        while self.move_up(inserted_index):
            inserted_index=inserted_index//2

        return True


    def pop(self):
        if len(self.heap_array)<=1:
            return False
        poped_node=self.heap_array[1]
        self.heap_array[1]=self.heap_array[-1]
        del self.heap_array[-1]

        poped_index=1
        while 1:
            left=poped_index*2
            right=poped_index*2+1

             #자식이 둘다 없을 때
            if left>(len(self.heap_array)-1):
                break
            #왼쪽 자식만 있을 때
            elif right > (len(self.heap_array)-1):
                if self.heap_array[poped_index]>self.heap_array[left]:
                    self.heap_array[left],self.heap_array[poped_index]=self.heap_array[poped_index],self.heap_array[left]
                    continue
                else:
                    break
            #자식이 둘 다 있을 때
            else : 
                # 자식 중 작은 노드와 변경
                if self.heap_array[right]<self.heap_array[left]:
                    if self.heap_array[right]<self.heap_array[poped_index]:
                        self.heap_array[right],self.heap_array[poped_index]=self.heap_array[poped_index],self.heap_array[right]
                        continue
                    else: 
                        break
                else:
                    if self.heap_array[left]<self.heap_array[poped_index]:
                        self.heap_array[left],self.heap_array[poped_index]=self.heap_array[poped_index],self.heap_array[left]
                        continue
                    else:
                        break
        return poped_node
        

# def solution(scoville, K):
    
#     #스코빌지수 입력
#     heap=Heap()
#     for i in scoville:
#         heap.insert(i)

#     if heap.heap_array[2]==0  &  heap.heap_array[1]==0 :
#         return -1
#     cnt=0
#     while (heap.heap_array[1]<K):
#         cnt+=1
#         min=heap.pop()
#         #print(heap.heap_array)
#         min_2nd=heap.pop()
#         score=min+(min_2nd*2)
#         heap.insert(score)
#     return cnt



# if __name__=="__main__":
#     scoville=[100, 0]
#     K=7
#     answer=solution(scoville,K)
#     print(answer)
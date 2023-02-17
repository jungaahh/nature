from heapq import heappush,heappop,heapify


def reverse(heap):
    reverse_heap=list()
    for _ in range(0,len(heap)):
        i=heappop(heap)
        reverse_heap.append(i*-1)
    heapify(reverse_heap)

    return reverse_heap

def solution(operations):
    heap=[]
    status_flag=-1
    for temp in operations:
        op,num=temp.split(' ')
        num=int(num)
        if op=='I':
            if status_flag==1:
                num=num*-1
            heappush(heap,num)
        else:
            if len(heap)==0:
                continue
            else:
                if status_flag==num:
                    heappop(heap)
                else:
                    heap=reverse(heap)
                    heappop(heap)
                    status_flag=num
    
    if len(heap)==0:
        return [0,0]
    elif len(heap)==1:
        return [heap[0],heap[0]]
    else:
        if status_flag==-1:
            a=heappop(heap) #최소
            b=heappop(reverse(heap))*-1 #최대
            return [b,a]
        else:
            a=heappop(heap) #최대
            b=heappop(reverse(heap)) #최소
            return [a*-1,b]
            



if __name__ =='__main__':
    
    operations=["I 1"]
  
 
    print(solution(operations))
    # # a=[1,2,3,4,5]
    # a.append(6)
    # print(a)

  
    # reverse_heap=[]
    # reverse_heap.append(45*-1)

    # print(reverse_heap)
def solution(numbers, target):
    answer = 0
    stop=len(numbers)
    visited_queue=[[0,0]]

    while len(visited_queue) > 0:
        index,node=visited_queue.pop()

        if index < stop:
            visited_queue.append([index+1,node+numbers[index]])
            visited_queue.append([index+1,node-numbers[index]])

        if index==stop:
            if node==target:
                answer+=1
    return answer

if __name__=="__main__":
    numbers=[4, 1, 2, 1]
    target=	2
    answer=solution(numbers,target)
    print(answer)

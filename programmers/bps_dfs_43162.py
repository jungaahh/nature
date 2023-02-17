def solution(n, computers):
    cnt=0
    visited_node=list()
    needed_node=list()
    needed_node.append(0)

    for i in range(0,n):
        if i in visited_node:
            continue
        needed_node.append(i)
        cnt+=1
        while needed_node:
            node=needed_node.pop()
            if node in visited_node:
                continue
            visited_node.append(node)
            for j in range(i,n):
                if (computers[node][j]) and (j not in visited_node):
                    needed_node.append(j)

    if len(visited_node)==n:
        return cnt
    



if __name__=="__main__":
    n=5
    #computers=[[1,0,0,1,1],[0,1,0,0,1],[0,0,1,0,1],[1,0,0,1,0],[0,1,1,0,1]] 
    #computers=[[1,1,0,0,1],[1,1,0,0,1],[0,0,1,1,1,],[0,1,1,1,0],[1,0,1,0,1]]
    computers=[[1,0,0],[0,1,0],[0,0,1]]
    answer=solution(len(computers), computers)
    print(answer)

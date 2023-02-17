
def calc(result_pre,present):
    new_result=[]
    
    for a in range(0,len(present)):
        
        if (a==0):
            #print('pre{}'.format(result_pre[0]+present[a]))
            # temp.append(result_pre[0][0]+present[a])
            new_result.append(result_pre[0]+present[a])
        elif a==(len(present)-1):
            # temp.append(result_pre[a-1][0]+present[a])
            new_result.append(result_pre[a-1]+present[a])
        else:
            # temp=[]
            # temp.extend([num + present[a] for num in result_pre[a-1]+result_pre[a]])
            new_result.append(present[a]+max(result_pre[a-1],result_pre[a]))

        # new_result.append(temp)
    return new_result

def solution(triangle):
    answer=0
    n=len(triangle)

    result=[]
    if n==1:
        return triangle[0][0]

    result.append(triangle[0])
    
    for i in range(1,n):
        result.append(calc(result[i-1],triangle[i]))
        
    return max(result[-1])

if __name__=="__main__":
    triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    solution(triangle)
    print(solution(triangle))
    
    # present=[1,2,3,4,5]
    # temp.extend([num + 1 for num in present])
    # print(temp)
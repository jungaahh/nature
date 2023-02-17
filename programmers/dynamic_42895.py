def calculate(X,Y):
    res=[]
    for x in X:
        for y in Y:
            res.append(x+y)
            res.append(x*y)
            res.append(x-y)
            if y!=0:
                res.append(x//y)
    
    return res


def solution(N, number):
    answer = -1
    
    result={}
    result[1]={N} ## memorize 결과 저장
    if N==number:
        return 1
    else:
        for n in range(2,8):
            temp_set=set()
            temp_set.add(int(str(N)*n))
            print(temp_set)
            i=1
            while i<n:
                temp_set.update(calculate(result[i],result[n-i])) #아직도 이부분이 이해가 안됨.. 하지만 이 조건으로 DP를 구현하기에, 중요한 조건인듯
                # print(temp_set)
                i+=1

            if number in temp_set:
                return n
            result[n]=temp_set
            print(result)
    
    return answer

if __name__=='__main__':
    N=2
    number=22222
    print(solution(N,number))
   
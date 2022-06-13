## 프로그래머 문제
## 해시부분
## 문제명 : 위장 (https://programmers.co.kr/learn/courses/30/lessons/42578)
## 작성일자 : 2022-03-09


## 풀이방법
# 1. 옷의 종류를 key, 명칭을 value list로 한 해시맵 생성
# 2. 총 경우의 수이므로 옷의 종류별 옷의 개수를 곱함. 
# 3. 아무것도 착용하지 않는건 허용하지 않으므로 마지막에 -1

##기본 dictionary 함수
def solution(clothes):
    answer = 1
    hash={}
    for c,t in clothes:
        if t in hash:
            hash[t].append(c)
        else:
            hash[t]=[c]

    for key in hash:
        answer*=(len(hash[key])+1)

    return answer-1 # 아무것도 착용하지 않는경우는 제외

##외부 라이브러리 함수
from collections import defaultdict
def solution_2(clothes):
    answer = 1
    hash=defaultdict(list) #기본값으로 value값을 list로 선언
    for cloth in clothes:
        hash[cloth[1]].append(cloth[0]) # key 존재빼고 바로 삽입할 수 있음

    for key in hash:
        answer*=(len(hash[key])+1)

    return answer-1

##외부 라이브러리 함수 길이로 수행
from collections import defaultdict
def solution_3(clothes):
    answer = 1
    hash=defaultdict(int) #기본값으로 value값을 list로 선언
    for c,t in clothes:
        hash[t]+=1 # key 존재빼고 바로 삽입할 수 있음

    for key in hash:
        answer*=(hash[key]+1)

    return answer-1


if __name__=='__main__':
    #clothes=[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
    print(solution_3(clothes))


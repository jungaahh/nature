## 프로그래머 문제
## 해시부분
## 문제명 : 전화번호 목록 (https://programmers.co.kr/learn/courses/30/lessons/42577)
## 작성일자 : 2022-03-09


## 풀이방법
# 1. 해시맵 생성
# 2. 문자열을 하나씩 추출하여 해당 key가 있다면 return false
#    - 주의사항 : 짧은 문자열에서 긴 문자열이 아닌, 긴 문자열로부터 짧은 문자열을 찾음
#      - ex) 1195524421 에서 하나씩 찾다보면 119가 도출되며 이를 찾으면 false로 리턴
#   * 시간복잡은 문자열 n개만큼 걸리긴 함..
#   * !!이 부분은 나중에 또 계산해 보겠음 !!

def solution(phone_book):
    answer = True
    
    # 리스트를 해시로 변환
    keys=dict.fromkeys(phone_book,0)

    # 앞의 내용이 hash map에 있는지 확인
    for number in phone_book:
        jubdoo=""
        for num in number:
            jubdoo+=num ## num
            if (jubdoo in keys) & (jubdoo!=number): #짧은 것에서 긴 것을 찾는게 아니라, 긴 부분에서 하나씩 추출하여 짧은게 있다면 찾은 것
                answer=False
                return answer

         
    return answer

if __name__ == '__main__':
    phone_book=["119", "97674223", "1195524421"]
    print(solution(phone_book))
    
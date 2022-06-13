## 프로그래머 문제
## 해시부분
## 문제명 : 베스트앨범 (https://programmers.co.kr/learn/courses/30/lessons/42579)
## 작성일자 : 2022-03-09


## 풀이방법
# 1. 옷의 종류를 key, 명칭을 value list로 한 해시맵 생성
# 2. 총 경우의 수이므로 옷의 종류별 옷의 개수를 곱함. 
# 3. 아무것도 착용하지 않는건 허용하지 않으므로 마지막에 -1


from collections import defaultdict

def solution(genres, plays):
    answer = []

    hash_genres=defaultdict(int)
    hash_num=defaultdict(list)
    for i in range(0,len(genres)):
        hash_num[genres[i]].append(i)
        hash_genres[genres[i]]+=plays[i]
        
    # play 총합순으로 장르 정렬
    sorted_genres= sorted(hash_genres.items(), key=lambda x: x[1],reverse=True) 
    first=sorted_genres[0][0]
    second=sorted_genres[1][0]

    # 최대값 찾기
    max=hash_num[first][0]
    semi_max=hash_num[second][0]
    for num in hash_num[first]:
        if plays[num]>plays[max]:
            semi_max=max
            max=num
        elif plays[num]==plays[max]:
            semi_max=num

    answer.extend([max,semi_max])



    # 최대값 찾기
    max=hash_num[second][0]
    semi_max=hash_num[second][0]
    for num in hash_num[second]:
        if plays[num]>plays[max]:
            semi_max=max
            max=num
        elif plays[num]==plays[max]:
            semi_max=num

    answer.extend([max,semi_max])


    return answer

if __name__=="__main__":
    genres=["classic", "pop", "classic", "classic", "pop"]
    plays=[500, 2500, 150, 800, 2500]
    print(solution(genres,plays))
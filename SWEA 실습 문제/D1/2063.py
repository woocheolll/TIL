# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.


N = int(input())
scores = list(map(int, input().split()))
scores.sort()

for i in range(N) :
    if i == N//2 :
        print(scores[i])
        break

# 1182 부분 수열의 합

from itertools import combinations

N, S = map(int, input().split())
int_list = list(map(int, input().split()))  

cnt = 0

# 모든 부분 집합을 생성하여 합이 S가 되는 경우를 카운트
for i in range(1, N+1):
    for subset in combinations(int_list, i):
        if sum(subset) == S:
            cnt += 1

print(cnt)


# 18353 병사 배치하기
# 제외시킬 병사의 수 출력
# LIS (Longest Increasing Subsequence) 사용
# https://mgyo.tistory.com/689 참고

n = int(input())
power = list(map(int, input().split()))

dp = [1] * n # 배열 초기화

# LIS 알고리즘을 이용하여 내림차순인 부분 수열의 최대 길이 구하기 
for i in range(1, n):
    for j in range(i):
        if power[i] < power[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))


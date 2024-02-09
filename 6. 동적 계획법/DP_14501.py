# 14501 퇴사
# n일 동안 최대 수익
# bottom up 방식 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] # arr[][0]: 일수, arr[][1]: 금액 

dp = [0] * (n + 1)  # 배열 초기화 

# 반복문 돌면서 인덱스가 가장 클 때의 값 = 최대의 값 
for i in range(n):
    # 상담을 진행하지 않는 경우, 이전 값 업데이트 
    dp[i + 1] = max(dp[i], dp[i + 1])
    
    # 상담을 진행하는 경우
    if i + arr[i][0] <= n:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])

print(dp[n])


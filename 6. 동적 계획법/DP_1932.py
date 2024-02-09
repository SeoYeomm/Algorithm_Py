# 1932 정수 삼각형
# bottom-up 방식 (현재에서 왼쪽 위, 오른쪽 위 중 큰 값 선택)
# 현재 (i, j), 왼쪽 위 (i-1, j-1), 오른쪽 위 (i-1, j)

n = int(input())
triangle = [list(map(int, input().split())) for i in range(n)]

dp = [[0] * n for _ in range(n)] # 배열 초기화
dp[0][0] = triangle[0][0]

# i = 높이, j = 밑변 
for i in range (1,n):
    for j in range(i+1):
        if j == 0:  # 왼쪽 끝 
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:  # 오른쪽 끝 
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:  # 중간 -> 왼쪽 위 대각선, 오른쪽 위 대각선 중 최대 선택 
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
print(max(dp[n-1]))


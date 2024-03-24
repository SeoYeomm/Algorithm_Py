MOD = 1000000007

def solution(n):
    # n이 홀수인 경우는 만들 수 없음
    if n % 2 != 0:
        return 0

    dp = [0] * (n + 1) # dp 배열 생성
    dp[0] = 1 # dp[0]=1로 초기화해줘야 안쪽 for문을 돌면서 마지막에 dp[0]*2로 매번 추가되는 케이스가 더해짐.
    dp[2] = 3

    for i in range(4, n + 1, 2): # (시작값, 끝값, 증가값) 
        dp[i] = dp[i - 2] * 3

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2
        dp[i] %= MOD
        
    return dp[n]

import sys
input = sys.stdin.readline

MOD = 1000000007

def solution(n):
    dp=[0]*(n+1)
    dp[2]=2
    dp[3]=3
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD
    return dp[n]

n = int(input())
print(solution(n))

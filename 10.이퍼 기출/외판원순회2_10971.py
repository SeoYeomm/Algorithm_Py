import sys
input = sys.stdin.readline

def backtrack(n, matrix, visited, cnt, cur_city, cost, ans):
    if cost >= ans:
        return ans
    
    if cnt == n: # 종료 조건: n개 도시 순회 
        if matrix[cur_city][0] != 0: # 출발도시(0)으로 돌아올 수 있는지 확인 
            ans = min(ans, cost + matrix[cur_city][0])
        return ans
    
    for i in range(n): # cur_city에서 도시 i로 이동
        # 0이면 False, 0이 아니면 True
        if matrix[cur_city][i] and not visited[i]: # 길이 있고 아직 방문하지 않은 도시이면  
            visited[i] = True
            ans = backtrack(n, matrix, visited, cnt + 1, i, cost + matrix[cur_city][i], ans)
            visited[i] = False
    
    return ans

def solution(n, matrix):
    visited = [False] * n
    visited[0] = True
    MAX = 1e8 # 최소 비용 저장을 위해 최댓값으로 초기화 
    ans = backtrack(n, matrix, visited, 1, 0, 0, MAX)
    return ans

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)] # 비용 행렬 
print(solution(n, matrix))

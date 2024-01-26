# 18405 경쟁적 전염
# S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류 출력, 없으면 0 출력 
# BFS
import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, s, target_x, target_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 바이러스 정보를 담는 리스트
    viruses = []

    # 초기 바이러스 정보를 리스트에 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                viruses.append((graph[i][j], 0, i, j))  # (바이러스 종류, 현재 시간, x좌표, y좌표)

    # 바이러스 숫자가 작은 순서대로 정렬 
    viruses.sort()
    
    # 큐에 초기 바이러스 정보를 넣음
    queue = deque(viruses)

    while queue:
        virus, second, x, y = queue.popleft()

        # s초가 지나면 종료
        if second == s:
            break

        # 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 빈 칸이면 바이러스 퍼뜨림
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, second + 1, nx, ny))
                
    return graph[target_x - 1][target_y - 1]

n, k = map(int, input().split()) # k: 바이러스 종류 
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())  # s: 초, (x, y): 좌표

result = bfs(graph, s, x, y)
print(result)

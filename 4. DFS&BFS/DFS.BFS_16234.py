#16234 인구 이동
# 두 나라의 인구 차이가 L명 이상, R명 이하라면, 국경선 오픈 
# 연합을 이루고 있는 각 칸의 인구수 = (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
# 인구 이동 며칠동안 이루어지는지 출력

from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph, n, l, r):
    # 상하좌우 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    days = 0 # 인구이동 발생 일수 

    def find_union(start_x, start_y): # bfs 탐색 시작 좌표 입력 
        queue = deque([(start_x, start_y)])
        country = [(start_x, start_y)] # 연합을 이루는 국가들 좌표
        total = graph[start_x][start_y] # 연합국 총 인구수 
        visited[start_x][start_y] = True # 방문 표시 

        while queue: 
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 방문하지 않았고 인구 차가 l명 이상 r명 이하인 경우 
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    queue.append((nx, ny)) # 다음에 방문할 국가로 추가 
                    country.append((nx, ny)) # 연합에 추가 
                    total += graph[nx][ny] 
                    visited[nx][ny] = True # 방문 표시 

        return country, total

    while True: 
        moved = False # 인구이동 여부 
        visited = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if not visited[i][j]: # 아직 방문 안했으면 
                    union, population = find_union(i, j) # 연합 찾기
                    
                    if len(union) > 1: # 연합이 생겼으면 
                        moved = True # 인구이동 발생
    
                        for x, y in union:
                            graph[x][y] = population // len(union) # 연합에 속한 국가들의 인구 이동 

        if not moved: # 인구 이동이 일어나지 않으면 반복문 빠져나옴 
            break

        days += 1
    return days

print(bfs(graph, N, L, R))

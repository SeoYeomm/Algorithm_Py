# 18352 특정 거리의 도시 찾기
# 최단거리 -> BFS -> 큐(덱)으로 구현

import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())  # 노드 개수, 도로 개수, 최단 거리, 출발 노드

distance = [-1] * (n + 1)  # 거리 정보를 담을 리스트, -1로 초기화

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start_v):
    deq = deque()
    deq.append((start_v, 0))  # 출발 노드와 거리를 함께 덱에 저장
    distance[start_v] = 0  # 출발 노드의 거리를 0으로 초기화
    
    while deq: # 덱이 비지 않으면
        v, dist = deq.popleft() # 첫번째로 들어온 노드 꺼내서 현재 탐색 중인 노드로 설정 
        
        for nei in graph[v]: # v와 연결된 이웃노드들 반복 
            if distance[nei] == -1:  # 아직 방문하지 않은 노드일 경우에만 거리 업데이트
                distance[nei] = dist + 1
                deq.append((nei, dist + 1))

bfs(x)

# 최단 거리가 k인 도시 출력
found_cities = [i for i in range(1, n + 1) if distance[i] == k]

if not found_cities:
    print(-1)
else:
    for city in found_cities:
        print(city)

# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴

import sys
import heapq as hq

input = sys.stdin.readline

def solution(lec):
    pq=[-1]
    lec.sort()

    for start, end in lec: 
        if pq[0]<=start: # 끝나는 시간과 start의 비교 
            hq.heappop(pq)
        hq.heappush(pq,end)
    return len(pq)

n = int(input())
lec = [tuple(map(int,input().split())) for _ in range (n)]
print(solution(lec))


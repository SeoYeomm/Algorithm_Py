import heapq
# heapq = 최소 힙(Min Heap), heap[0]이 최소값 
n = int(input())
card  = []

for i in range (n):
    heapq.heappush(card, int(input()))
# 적은 개수부터 더하면 최소 횟수가 됨

sum = 0
while len(card)>1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum = sum+ a + b
    heapq.heappush(card, a + b)

print (sum)

'''
시간 초과

n = int(input())
card = []

for i in range(n):
    card.append(int(input()))

sum = 0

while len(card) > 1:
    card.sort(reverse=True) 
    a = card.pop()
    b = card.pop()
    sum += a + b
    card.append(a + b)

print(sum)

'''

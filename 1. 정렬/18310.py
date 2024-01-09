# 안테나로부터 모든 거리의 합이 최소가 되도록
n = int(input())
loca = list(map(int, input().split())) # 문자열 리스트 -> 정수 리스트 

# 중간에 있는 지점이 항상 최소가 됨
loca.sort()
center = (n-1)//2
print(loca[center])

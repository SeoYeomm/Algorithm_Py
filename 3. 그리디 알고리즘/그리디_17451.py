#17451 평행우주
# 지구에서 출발하는 최소 속도 구하기
#도착지 -> 출발지로 역순해서 최소 속도 출력

import math
n= int(input())
v = list(map(int, input().split())) 
v.reverse() 
min_v =1

for p in v:
    if(p>=min_v):
        min_v=p # 최소 속도 갱신 
    elif ((min_v%p)!=0): # 필요한 속도의 정수배가 아니면 
        min_v=(math.ceil(min_v/p))*p # 필요한 속도의 정수배 중 최소로 만들어줌  

print(min_v)
        

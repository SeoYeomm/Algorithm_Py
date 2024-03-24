# 바퀴 시계방향 -> 화살표 반시계 
# 출력은 시계방향 

import sys
input = sys.stdin.readline

def solution(n,record):
    wheel = ['?']*n
    is_available = dict()

    ord_a = ord('A')
    for i in range(26):
        is_available[chr(i+ord_a)]=True

    idx = 0 # 화살표가 가르키는 인덱스

    for rot,alpha in record:
        idx = (idx-int(rot))%n # 화살표는 반시계로 

        if wheel[idx]==alpha:
            continue

        if wheel[idx] != '?' or not is_available[alpha]:
            return '!'
        
        wheel[idx]=alpha
        is_available[alpha]=False # 해당 알파벳 사용했다 

    return ''.join(wheel[idx:]+wheel[:idx]) # 출력은 시계로 

n,k = map(int,input().split())
record = [input().split() for _ in range(k)]

print(solution(n,record))

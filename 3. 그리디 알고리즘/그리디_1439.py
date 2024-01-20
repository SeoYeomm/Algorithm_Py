#1439 뒤집기 
# 문자열의 모든 수를 같게 하는 최소 횟수
#반례: 1010 -> 답: 2
#반례: 01110011 -> 답: 2 

s = input()
L = len(s)
cnt = 0

for i in range(L - 1):
    if s[i] != s[i + 1]:
        cnt += 1

# 시작과 끝이 다른 경우도 연속하지 않은 걸로 고려
if s[-1] != s[0]:
    cnt += 1

print(cnt // 2)

'''
if (cnt%2==0):
    print(cnt // 2)
else:
    print(cnt)
'''

    

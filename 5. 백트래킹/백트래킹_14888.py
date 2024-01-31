# 14888 연산자 끼워넣기
# 연산자 순서 무시하고 앞에서부터 순서대로 계산

N = int(input())
arr = list(map(int, input().split()))
calc = list(map(int, input().split()))  # 더하기, 빼기, 곱하기, 나누기 
ans = []

def backtrack(num, idx):
    
    if idx == N: # N-1 인덱스의 숫자까지 연산한 경우 재귀 호출 종료
        ans.append(num)
        return
    
    for i in range(4):
        if calc[i] != 0:
            calc[i] -= 1 # 연산자 사용 
             
            if i == 0: # 덧셈 
                backtrack(num + arr[idx], idx + 1)
            elif i == 1: # 뺄셈 
                backtrack(num - arr[idx], idx + 1)
            elif i == 2: # 곱셈 
                backtrack(num * arr[idx], idx + 1)
            elif i == 3:  # 나눗셈 
                if num >= 0:
                    backtrack(num // arr[idx], idx + 1)
                # 음수를 양수로 나눌 때 
                else:
                    backtrack(-(-num // arr[idx]), idx + 1)
                    
            calc[i] += 1 # 연산자 반납 

backtrack(arr[0], 1)

print(max(ans))
print(min(ans))


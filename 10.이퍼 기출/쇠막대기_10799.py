import sys
input = sys.stdin.readline

def solution(s):
    answer = 0
    stack =[]

    for i in range(len(s)):
        if s[i]=="(":
            stack.append("(")
            
        else: # 닫힌 괄호인 경우 
            stack.pop()

            if s[i-1] == "(": # 레이저인 경우
                answer += len(stack)
            else: # 쇠막대기의 끝인 경우
                answer +=1

    return answer

s = input().rstrip()
print(solution(s))
                
                

import sys
from collections import Counter

input = sys.stdin.readline

def make (text):
    part1 =""
    part2 =""

    alphabets = sorted(Counter(text).items())

    for key, value in alphabets:
        if value%2==1:
            if len(part2)==1: # 만약 가운데 글자가 있다면 더 이상 불가능
                return "I'm Sorry Hansoo"
            part2 = key
        part1 += key*(value//2) #주의 

    return part1+part2+part1[::-1] # 역순 출력 

text = input().rstrip()
print(make(text))

# Counter(text): 각 문자가 몇개씩 들어있는지 dictionary 형태로 돌려줌
# .items() : key와 value를 짝 지어서 돌려줌
# sorted - 사전적으로 가장 앞서는 문자열을 만들기 위해 정렬
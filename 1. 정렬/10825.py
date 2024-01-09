n = int(input())
list1 = []

# 국어 점수 감소, 영어 점수 증가, 수학 점수 감소, 사전 순 증가하는 순서로 

for i in range(n):
    data = input().split()  # 입력에서 공백을 기준으로 나누어 리스트 생성 
    name = data[0] 
    kor = int(data[1])
    eng = int(data[2])
    math = int(data[3])
    list1.append([name, kor, eng, math])

# reverse=True로 설정 -> 내림차순으로
# 국어, 수학: 내림차순  영어, 이름: 오름차순으로

list1.sort(key=lambda x: (-x[1], x[2], -x[3], x[0])) 

for i in list1:
    print(i[0], end = '\n')

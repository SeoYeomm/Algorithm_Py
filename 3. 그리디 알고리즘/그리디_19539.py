#19539 사과나무
# 반례: 9 8 3 3 3 1 3 7 7 1 -> YES

n = int(input())
h = list(map(int, input().split()))

cnt2 = sum([x // 2 for x in h])
cnt1 = sum([x % 2 for x in h])

# 2가 1+1 될 때마다 cnt2: -1, cnt1: +2
# (cnt2-cnt1)가 3의 배수여야 둘이 같은 횟수로 뿌려짐

if (cnt2 >= cnt1 and (cnt2-cnt1)%3 == 0):
    print("YES")
else:
    print("NO")




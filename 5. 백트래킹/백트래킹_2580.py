# 2580 스도쿠
# 일단 가능한 숫자를 넣어보고 안되면 다른 숫자를 넣어봐요! 그나저나 같은 구역인지는 어떻게 알까요?
# 같은 구역의 크기는 3 x 3 이네요! N-queen 문제와 비슷하게 접근해볼까요?

graph = [list(map(int, input().split())) for _ in range(9)]

def check_row(r, n): # 각 행에 n인 숫자 있는지 체크 
    for i in range(9):
        if graph[r][i] == n:
            return False # 해당 행에 중복되는 숫자 있으면 
    return True
        
def check_col(c, n): # 각 열에 n인 숫자 있는지 체크 
    for i in range(9):
        if graph[i][c] == n:
            return False # 해당 열에 중복되는 숫자 있으면 
    return True

def check_square(r, c, n):
    start_r = r // 3 * 3 # 각 3x3 정사각형의 시작 좌표 
    start_c = c // 3 * 3 # (0,0), (3,0), (6,0), (3,0), (3,3), (6,3), (0,6), (3,6), (6,6)

    for i in range(3):
        for j in range(3):
            if graph[start_r + i][start_c + j] == n:
                return False # 해당 정사각형에 중복되는 숫자 있으면
    return True
    
def check(r, c, n): # 행과 열, 3x3 정사각형에 n인 숫자가 있는지 체크 
    return check_row(r, n) and check_col(c, n) and check_square(r, c, n)

def backtrack(idx):
    if idx == 9*9: # 81개의 칸 돌기 
        return True

    r = idx // 9
    c = idx % 9

    if graph[r][c] != 0: #비어있지 않으면 다음 칸으로 넘어감 
        return backtrack(idx + 1)
        
    for i in range(1, 10): # 숫자 채워넣기 
        if check(r, c, i):
            graph[r][c] = i
            
            if backtrack(idx + 1): # 다음 칸이 스도쿠 가능하면 
                return True # 현재 상태 유지
            
            else: # 다음 칸 스도쿠 안되면 
                graph[r][c] = 0 # 현재 칸 비우고 for문에서 다음 숫자 채워넣기  

    # for문 안에 모든 숫자가 불가능하면 이전 단계로 돌아감             
    return False 

backtrack(0)
for row in graph:
    print(*row)

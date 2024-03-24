size = 9

check_row = [[False] *(size+1) for _ in range(size)]
check_col = [[False] *(size+1) for _ in range(size)]
check_3x3 = [[False] *(size+1) for _ in range(size)]

def calc_area(x,y):
    return (x//3) *3 + (y//3)

def fill (cnt, board):
    if cnt == size* size:
        return True

    x, y = cnt//size, cnt%size

    if board[x][y]>0:
        # 이미 숫자 있으면 다음 칸으로 넘어감 
        return fill (cnt+1, board)# 주의 

    for i in range (1, size+1):
        # 행, 열, 3x3 사각형에 숫자 이미 있는지 확인 
        if check_row [x][i] or check_col [y][i] or check_3x3[calc_area(x,y)][i]: # 주의 
            continue
        
        check_row [x][i] = True
        check_col [y][i] = True
        check_3x3[calc_area(x,y)][i] = True
        board[x][y] = i

        if fill (cnt+1, board):
            return True

        check_row [x][i] = False
        check_col [y][i] = False
        check_3x3[calc_area(x,y)][i] = False
        board[x][y] = 0
    return False

def solution (board):
    ans = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            
            if board[i][j] == 0:
                continue
            ans [i][j] = board[i][j]
            # 주의 
            check_row [i][board[i][j]] = True
            check_col [j][board[i][j]] = True
            check_3x3[calc_area(i, j)][board[i][j]] = True

    fill (0, ans)
    return ans 

sudoku = [list(map(int, input().split())) for _ in range(size)]  
for line in solution(sudoku):
    print(*line)
    

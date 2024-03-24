from collections import deque

def game(n, board, cmd):
    # 우, 상, 좌, 하
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 뱀 초기화 (뱀이 있는 위치는 1, 사과는 2)
    snake = deque([(0, 0)])
    board[0][0] = 1

    t = 0 # 시간 
    head = 0  # 뱀의 머리 방향

    while True:
        t += 1
        # 뱀의 머리가 위치하게될 칸
        nr = snake[0][0] + dr[head]
        nc = snake[0][1] + dc[head]

        # 게임 종료 조건: 벽에 부딪히거나, 자기자신의 몸과 부딪힘
        if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] == 1:
            break

        if board[nr][nc] != 2:  # 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
            r, c = snake.pop()
            board[r][c] = 0

        # 사과가 있으면 몸길이를 늘림 
        snake.appendleft((nr, nc))
        board[nr][nc] = 1

        # 이번에 방향을 변환하는지 확인
        if t in cmd:
            if cmd[t] == 'L':  # 왼쪽 회전
                head = (head + 1) % 4
            if cmd[t] == 'D':  # 오른쪽 회전
                head = (head + 3) % 4
    return t

def solution(n, k, l, apples, rotation_t, rotation_d):
    board = [[0] * n for _ in range(n)]
    for x, y in apples:  
        board[x - 1][y - 1] = 2  # 사과 표시

    cmd = dict(zip(rotation_t, rotation_d))  # 시간, 회전 정보 저장
    answer = game(n, board, cmd)
    return answer

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())    # NxN , M 번 돌 놓음
    dol = [list(map(int, input().split())) for _ in range(M)]   # (x, y) , 1:흑, 2:백

    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2

    for t in dol :
        si, sj = t[1] - 1 , t[0] - 1
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, 1], [1, -1]] :
            n = 1
            last_i = -1
            is_osl = False
            while True :
                ni, nj = si + (di*n), sj + (dj*n)
                if 0 <= ni < N and 0 <= nj < N and board[ni][nj] :
                    if n == 1 and board[ni][nj] != t[2] :
                        is_osl = True

                    if not is_osl :
                        break
                    elif n >= 2 :
                        if board[ni][nj] != t[2] :
                            pass
                        else :
                            last_i = n
                else :
                    is_osl = False
                    break
                if last_i != -1 :
                    break

                n += 1

            if last_i != -1 :
                for n in range(0, last_i) :
                    board[si + (di*n)][sj + (dj*n)] = t[2]

    B_count = 0
    W_count = 0
    for i in range(N) :
        for j in range(N) :
            if board[i][j] == 1 :
                B_count += 1
            elif board[i][j] == 2 :
                W_count += 1

    print(f'#{tc} {B_count} {W_count}')
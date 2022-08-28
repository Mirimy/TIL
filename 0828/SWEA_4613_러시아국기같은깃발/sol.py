import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())    # N = i, M = j
    arr = [list(input()) for _ in range(N)]

    # chng = i 열을 ['W', 'B', 'R'] 색으로 할 때 바꿔야 하는 칸 수
    chng = [[0,0,0] for _ in range(N)]

    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == 'W' :
                chng[i][1] += 1
                chng[i][2] += 1
            elif arr[i][j] == 'B' :
                chng[i][0] += 1
                chng[i][2] += 1
            elif arr[i][j] == 'R' :
                chng[i][0] += 1
                chng[i][1] += 1

    counts = 0
    min_counts = N * M
    for Bis in range(1, N - 1) :        # 'B' 시작 줄   Bis idx = 1 ~ N-2  까지
        for Bie in range(Bis, N - 1) :  # 'B' 끝나는 줄 Bie idx = Bis ~ N-2 까지
            counts = 0
            for i in range(N) :
                if i < Bis:
                    counts += chng[i][0]
                elif Bis <= i <= Bie :
                    counts += chng[i][1]
                elif i > Bie :
                    counts += chng[i][2]

            if counts < min_counts :
                min_counts = counts

    print(f'#{tc} {min_counts}')
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr90 = [[0] * N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            arr90[j][N - i - 1] = arr[i][j]

    arr180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr180[j][N - i - 1] = arr90[i][j]

    arr270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr270[j][N - i - 1] = arr180[i][j]

    print(f'#{tc}')
    for i in range(N) :
        for j in range(N) :
            print(arr90[i][j], end='')
        print(' ', end='')
        for k in range(N) :
            print(arr180[i][k], end='')
        print(' ', end='')
        for l in range(N) :
            print(arr270[i][l], end='')
        print()
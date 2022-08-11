import sys

sys.stdin = open('input.txt')

# NxN 배열 5 <= N <= 15
# MxM 파리채 2 <= M <= N

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_die = 0

    # 파리채 시작 위치 [i][j]
    for i in range(0, N-M+1) :
        for j in range(0, N-M+1) :
            # 각 시작위치마다 죽은 파리 수 count
            die = 0
            # 시작 위치에서 행, 열 M 만큼 순회
            for k in range(i, i+M) :
                for l in range(j, j+M) :
                    die += arr[k][l]
            # 시작 위치에 따라 죽은 파리 max 값 저장
            if die > max_die :
                max_die = die

    print(f'#{tc} {max_die}')
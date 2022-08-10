import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    near_sum = 0
    for i in range(N) :
        for j in range(N) :
            for k in range(4) :
                near_i = i + di[k]
                near_j = j + dj[k]
                if 0 <= near_i < N and 0 <= near_j < N :
                    near_sum += abs(arr[i][j] - arr[near_i][near_j])

    print(f'#{tc + 1} {near_sum}')
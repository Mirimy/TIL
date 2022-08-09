import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T) :
    N, M = map(int, input().split())

    a = list(map(int, input().split()))

    min_sum = 10000 * M
    max_sum = 0
    for idx in range(N - M + 1) :
        # print(idx)
        # sum_value = a[idx] + a[idx+1] + a[idx+2]
        sum_value = 0
        for i in range(idx, idx + M) :
            sum_value += a[i]

        if sum_value > max_sum :
            max_sum = sum_value

        if sum_value < min_sum :
            min_sum = sum_value
    result = max_sum - min_sum
    print(f'#{tc + 1} {result}')
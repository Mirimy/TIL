import sys

sys.stdin = open('input.txt')


for _ in range(10) :
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    for i in range(100) :
        sum_x = sum_y = sum_cross_right = sum_cross_left= 0
        for j in range(100) :
            # 행/열에서 i 값 고정일 때 각 행/열 누계
            sum_x += arr[i][j]
            sum_y += arr[j][i]

            # i = j 혹은 i + j = 99 일 때 대각선 요소 누계
            if i == j:
                sum_cross_right += arr[i][j]
            if i + j == 99:
                sum_cross_left += arr[i][j]

    # 저장해둔 값이 최댓값인가?
        if sum_x > max_sum :
            max_sum = sum_x
        if sum_y > max_sum :
            max_sum = sum_y

    if sum_cross_right > max_sum :
        max_sum = sum_cross_right
    if sum_cross_left > max_sum :
        max_sum = sum_cross_left

    print(f'#{tc} {max_sum}')



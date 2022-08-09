import sys

sys.stdin = open('input.txt')

for tc in range(10) :
    dump = int(input())
    h = list(map(int, input().split()))


    box_floor = [0] * 100
    for i in h :
        for j in range(i) :
            box_floor[j] += 1

    # print(box_floor)

    max_floor = 100
    min_floor = 0

    high_sum = low_sum = 0

    for k in box_floor[::-1] :
        # 높은 위치
        if high_sum < dump :
            high_sum += k
            max_floor -= 1
        else :
            break

        if high_sum > dump :
            max_floor += 1

    for l in box_floor :
        # 낮은 위치
        if low_sum < dump :
            low_sum += (100 - l)
            min_floor += 1
        else :
            break

        if low_sum > dump :
            min_floor -= 1

    result = max_floor - min_floor
    print(f'#{tc + 1} {result}')

import sys

sys.stdin = open('input.txt')

for tc in range(1, 11) :
    N = int(input())
    building = list(map(int, input().split()))

    sum_value = 0
    for i in range(2, len(building) - 1) :
        min_value = 255
        for j in range(i-2, i+3) :
            if i == j :
                continue
            elif building[i] - building[j] <= 0 :
                min_value = 0
                break
            elif building[i] - building[j] < min_value :
                min_value = building[i] - building[j]


        sum_value += min_value
    print(f'#{tc} {sum_value}')



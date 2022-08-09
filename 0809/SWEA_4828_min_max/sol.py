import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T) :
    N = int(input())
    num_lst = list(map(int, input().split()))

    max_num = 1
    min_num = 1000000
    for i in num_lst :
        if i > max_num :
            max_num = i

        if i < min_num :
            min_num = i

    print(f'#{tc + 1} {max_num - min_num}')

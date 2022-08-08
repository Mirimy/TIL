import sys

sys.stdin = open('input.txt')

N = int(input())

for tc in range(1, N+1) :
    A = int(input())

    numbers = list(map(int, input().split()))

    # print(tc, A, numbers)

    max_count = 0
    for i in range(len(numbers)) :
        counts = 0
        for j in range(len(numbers)) :
            if i < j and numbers[i] > numbers[j] :
                counts += 1
        if counts > max_count :
            max_count = counts

    print(f'#{tc} {max_count}')
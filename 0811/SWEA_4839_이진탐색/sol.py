import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    P, A, B = map(int, input().split())

    count_A = count_B = 0

    # A 이진탐색
    start = 1
    end = P
    while start <= end :
        middle = (start + end) // 2
        if A == middle :
            break
        elif start + 1 == end and end == P:
            start += 1
        elif A > middle :
            start = middle
            count_A += 1
        else :
            end = middle
            count_A += 1
    # B 이진탐색
    start = 1
    end = P
    while start <= end :
        middle = (start + end) // 2
        if B == middle :
            break
        elif start + 1 == end and end == P:
            start += 1
        elif B > middle :
            start = middle
            count_B += 1
        else :
            end = middle
            count_B += 1



    print(count_A, count_B)

    # 비교하여 결과 출력
    if count_A < count_B :
        result = 'A'
    elif count_A > count_B :
        result = 'B'
    else :
        result = 0
    print(f'#{tc} {result}')
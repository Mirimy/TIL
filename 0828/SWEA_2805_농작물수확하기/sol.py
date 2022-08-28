import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())        # N 농장의 크기(홀수)
    arr = [list(map(int, input())) for _ in range(N)]

    middle = N // 2         # 가운데 인덱스 값
    s = 0
    i = 0
    lr = -1
    while i < N :
        if i <= middle :    # 가운데 제일 긴 줄 까지
            lr += 1
        else :              # 가운데 제일 긴 줄 밑에부터
            lr -= 1

        for j in range(middle - lr, middle + lr + 1):
            s += arr[i][j]
        i += 1

    print(f'#{tc} {s}')

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T) :
    N = int(input())

    # N * N 의 2차원 리스트 만들기
    arr = []
    for i in range(N):
        empty = []  # 안쪽 리스트로 사용할 빈 리스트 생성
        for j in range(N):
            empty.append(0)  # 안쪽 리스트에 0 추가
        arr.append(empty)

    num = 1
    start = 0
    end = N

    while num < (N * N) + 1:
        # 위치 정중앙일때
        if start == end - 1:
            arr[start][end-1] += num
            num += 1
            break
        # 그 외 ( 사각형 오른쪽 -> 아래 -> 왼쪽 -> 위 순으로 진행)
        else:
            # 오른쪽
            for j in range(start, end):
                arr[start][j] += num
                if j != end - 1:
                    num += 1
            # 아래
            for i in range(start, end):
                # 처음 아니면
                if i != start:
                    arr[i][end - 1] += num
                # 마지막 아니면
                if i != end - 1:
                    num += 1
            # 왼쪽
            for j in range(start, end):
                if j != start:
                    arr[end - 1][N - j - 1] += num
                if j != end - 1:
                    num += 1
            # 위
            for i in range(start, end):
                if i != start and i != end - 1:
                    arr[N - i - 1][start] += num
                if i != end - 1:
                    num += 1
        start += 1
        end -= 1

    print(f'#{tc+1}')
    for i in arr :
        for j in i :
            print(j, end=' ')
        print()
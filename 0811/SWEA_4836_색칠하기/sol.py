import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    # 10 x 10 의 0으로 이루어진 2차원 배열 만들기
    arr= []
    for o in range(10) :
        lst = []
        for i in range(10) :
            lst.append(0)
        arr.append(lst)

    for _ in range(N) :
        # start i, j / end i, j / color 값 받기
        si, sj, ei, ej, color = map(int, input().split())

        # start [i,j] 부터 end [i,j] 까지 영역 순회하여 color 값 +
        for i in range(si, ei+1) :
            for j in range(sj, ej+1) :
                # 해당 위치의 색상 값과 지금 더해주려는 색상 값이 다를 때만 더해준다.
                if arr[i][j] != color :
                    arr[i][j] += color


        # 보라색 영역 (1 + 2 = 3) 카운트
        purple = 0
        for i in arr :
            for j in i :
                if j == 3 :
                    purple += 1

    print(f'#{tc} {purple}')
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 시작위치(si, sj), 도착위치(ei, ej) 찾기
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 2 :
                si, sj = i, j
            elif arr[i][j] == 3 :
                ei, ej = i, j
    # 상하좌우 델타 값
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    stack = []

    while True : # 3 나올때까지
        visited[si][sj] = 1                 # visited 방문 위치 저장
        if visited[ei][ej] == 1 :           # 도착위치 방문했으면 성공, break
            result = 1
            break

        for d in range(4) :                 # 상하좌우 델타 순회하며 1. 갈 수 있고, 2. 방문 안 한 곳 stack에 저장
            if si == 0 and d == 0 :         # index error 방지 조건
                continue
            elif si == N - 1 and d == 1 :
                continue
            elif sj == 0 and d == 2 :
                continue
            elif sj == N - 1 and d == 3 :
                continue
            if (arr[si + di[d]][sj + dj[d]] == 0 or arr[si + di[d]][sj + dj[d]] == 3) and visited[si + di[d]][sj + dj[d]] == 0:
                stack.append([si + di[d], sj + dj[d]])

        if stack :                          # stack에서 다음 갈 곳 좌표 뽑기
            nxt = stack.pop()
            si = nxt[0]
            sj = nxt[1]
        else :                              # 갈 곳 없으면 실패, break
            result = 0
            break


    print(f'#{tc} {result}')
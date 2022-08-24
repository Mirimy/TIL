import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == 2 :                # 시작위치 [si, sj] 저장
                si, sj = i, j
            elif maze[i][j] == 3 :              # 도착위치 [ei, ej] 저장
                ei, ej = i, j

    visited = [[0] * N for _ in range(N)]
    q = []
    visited[si][sj] = -1                        # 처음 시작위치 -1 저장
    while not visited[ei][ej] :                 # BFS라 거리 1인곳 -> 2인곳-> 3... 이런식으로 가기 때문에
                                                # 도착 위치에 숫자 찍혔을 때 바로 탈출하면 최단 거리
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]] :      # 델타 탐색
            ni, nj = si + di, sj + dj                           # 다음 위치 정하기
            # 큐에 담을 조건
            # 1. idx error 나지 않을 것
            # 2. 벽( 1 ) 이 아닐 것
            # 3. visited 방문하지 않은 곳
            if 0 <= ni < N and 0 <= nj < N and (maze[ni][nj] != 1) and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[si][sj] + 1

        if q :                      # 다음 위치 뽑기
            si, sj = q.pop(0)
        else :                      # 갈 곳 없으면 break
            break

    result = visited[ei][ej]

    print(f'#{tc} {result}')
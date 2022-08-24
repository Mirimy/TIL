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
    while True :
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]] :      # 델타 탐색
            ni, nj = si + di, sj + dj                           # 다음 위치 정하기
            # 큐에 담을 조건
            # 1. idx error 나지 않을 것
            # 2. 벽( 1 ) 이 아닐 것
            # 3. visited 방문하지 않은 곳이거나, 방문했더라도 지금 내가 저장하려는 최단 거리보다 큰 숫자일 것 (<-이 때는 덮어쓰려고)
            if 0 <= ni < N and 0 <= nj < N and (maze[ni][nj] != 1) and (visited[ni][nj] == 0 or visited[ni][nj] > visited[si][sj] + 1):
                q.append([ni, nj])
                visited[ni][nj] = visited[si][sj] + 1

        if q :                      # 다음 위치 뽑기
            si, sj = q.pop()        # BFS로 풀려고 했는데 쓰다 보니 ..;; pop(0)으로 해도 되긴 함
        else :                      # 갈 곳 없으면 break
            break

    result = visited[ei][ej]

    print(f'#{tc} {result}')


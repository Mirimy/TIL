import sys
sys.stdin = open('input.txt')

for _ in range(1, 11) :
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # ================= 미로 시작/도착 위치 찾기 ======================
    for i in range(16) :
        for j in range(16) :
            if maze[i][j] == 2 :
                si, sj = i, j
            elif maze[i][j] == 3 :
                ei, ej = i, j
    # ====================== 길 찾기 ======================
    visited = [[0] * 16 for _ in range(16)]
    stack = []
    while True :
        visited[si][sj] = 1
        if visited[ei][ej] :
            break

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
            ni, nj = si + di, sj + dj
            # stack에 넣을 조건
            # 1. 인덱스 에러 나지 않을 것
            # 2. 벽( 1 ) 이 아닐 것
            # 3. 방문했던 곳이 아닐 것
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and not visited[ni][nj] :
                stack.append([ni, nj])

        if stack :
            si, sj = stack.pop()
        else :
            break

    print(f'#{tc} {visited[ei][ej]}')

import sys
sys.stdin = open('input.txt')

for _ in range(1, 11) :
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(16) :
        for j in range(16) :
            if maze[i][j] == 2 :
                si, sj = i, j
            elif maze[i][j] == 3 :
                ei, ej = i, j

    visited = [[0] * 16 for _ in range(16)]
    q = []
    while True :
        visited[si][sj] = 1
        if visited[ei][ej] :
            break

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
            ni, nj = si + di, sj + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and not visited[ni][nj] :
                q.append([ni, nj])

        if q :
            si, sj = q.pop(0)       # DFS랑 같은데 여기만.. pop(0) 으로
        else :
            break

    print(f'#{tc} {visited[ei][ej]}')
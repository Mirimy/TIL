import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    V, E = map(int, input().split())

    route = []
    for i in range(V+1) :
        route.append([])
        for j in range(V+1) :
            route[i].append(0)

    for _ in range(E) :
        a, b = map(int, input().split())
        route[a][b] = 1
        route[b][a] = 1

    S, G = map(int, input().split())

    visited = [False] * (V+1)
    stack = [S]

    while True:
        S = stack.pop()
        if visited[S] == False :
            visited[S] = True       # 시작위치 visited에 표시

            if visited[G]:          # 도착위치 방문했으면 1 출력
                print(f'#{tc} 1')
                break

            for end in range(1, V+1) :    # 1 ~ 마지막번호 까지
                if route[S][end] == 1 and visited[end] == False :   # 시작위치 S 에서 갈 수 있으면
                    stack.append(end)     # stack []에 추가

        if stack == [] :            # 더이상 갈 곳 없으면 0 출력
            print(f'#{tc} 0')
            break
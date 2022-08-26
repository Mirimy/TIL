import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    V, E = map(int, input().split())    # V:노드 E:간선
    VE = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())  # S:출발 G:도착

    route = [[0] * (V+1) for _ in range(V+1)]

    for s, e in VE :            # 경로 route(2차원 배열)에 갈 수 있는 곳 : 1로 저장
        route[s][e] = 1
        route[e][s] = 1

    visited = [0] * (V + 1)     # 방문했던 곳 + 온 거리 저장
    q = []                      # 다음 방문할 곳 리스트

    while visited[G] == 0 :     # BFS이기 때문에 도착위치 방문이 확인되면 바로 탈출
        for end in range(1, V + 1) :
            if route[S][end] and not visited[end] :     # 시작위치 S에서 갈 수 있는 곳 ?
                q.append(end)                           # q에 저장
                visited[end] = visited[S] + 1           # visited에 온 거리 저장

        if q :                  # 다음 갈 곳 (q) 있으면?
            S = q.pop(0)        # pop(0)
        else :                  # 없으면 ?
            break               # 실패, 탈출

    print(f'#{tc} {visited[G]}')

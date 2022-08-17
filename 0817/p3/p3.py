# DPS 연습문제
import sys
sys.stdin = open('input.txt')

# 시작하는 정점 정보 전달 받아서
def DFS(start) :
    # 다음 조사 위치 쌓아 나가기 위해서
    stack = [start]
    # 한 번 방문했던 곳 재방문하지 않도록 하기위한
    # 방문 가능한 크기만큼
    # 기본적으로 방문 안했음이 default 이므로 0 으로 초기화
    visited = [0] * (V + 1)    # range 0 부터라서 1 더해줌


    # 전수조사 시작할건데
    # 언제까지 조사할 것이냐
    # stack이 빌 때까지
    while stack :
        # 내 조사 대항 == stack의 마지막 정점
        start = stack.pop()

        # 해당 정점이 아직 방문하기 전이라면
        if visited[start] == 0 :
            # 일단 방문
            visited[start] == 1
            print(stack)
            print(start, visited)

            # 모든 정점들 조사
            for next in range(1, V+1) :
                # start 번째 기준으로 next가 이동 가능하고
                # next 번째가 방문하기 전이라면
                if G[start][next] == 1 and visited[next] == 0 :
                    # stack에 next 정점 추가
                    stack.append(next)


# V : 정점 E : 간선
V, E = map(int, input().split())
data = list(map(int, input().split()))
print(V,E)
print(data)

G = [[0 for _ in range(E)] for _ in range(E)]

for i in range(E) :
    '''
    경로 나타내기
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1
    '''
    # 앞쪽에 들어갈 값 0 2 4 6 8 10
    # 뒤쪽 1 3 5 7 9 11
    G[data[i*2]][data[i*2+1]] = 1
    # G[data[i*2+1]][data[i*2]] = 1

DFS(1)
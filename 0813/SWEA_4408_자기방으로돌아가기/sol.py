import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    routes = []    # = [[시작,도착],[시작,도착],...] 루트 2차원 배열
    for _ in range(N) :
        a = list(map(int, input().split()))
        routes.append(a)

    for i in range(N):
        for j in range(2):
            routes[i][j] = (routes[i][j] + 1) // 2

    count = [0] * 200

    for route in routes :    # 루트 하나씩에 대해
        if route[0] < route[1] :    # end 방번호가 더 큰 경우
            for i in range(route[0]-1, route[1]) :    # 루트의 시작 ~ 끝 방까지
                count[i] += 1             # count 배열에 경로 1 추가
        else :
            for j in range(route[0]-1, route[1]-2, -1) :  # start 번호가 더 큰 경우!!! (ex : 400,300)
                count[j] += 1

    max_count = 0
    for i in count :
        if i > max_count :
            max_count = i       # 경로 count 배열에 max를 찾은 이유? 만약 4가 max 면 최소 4 단위시간 필요함


    print(f'#{tc} {max_count}')

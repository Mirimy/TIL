import sys
sys.stdin = open('input.txt')

for _ in range(10) :
    tc, N = map(int, input().split())
    # -------------- 입력받은 경로로 배열 만들기 ----------------
    route = []
    for _ in range(100) :      # 경로 표시할 100x100 짜리 2차원 배열 만들기
        arr = []
        for _ in range(100) :
            arr.append(0)
        route.append(arr)

    a = list(map(int, input().split()))     # 입력받은 데이터들 -> 리스트
    for i in range(0, N*2 , 2) :            # 2칸씩 끊어서
        route[a[i]][a[i+1]] = 1             # 일방통행 저장

    # ------------------------- DFS ------------------------
    visited = [0] * 100
    stack = [0]
    S = 0
    while True :
        S = stack.pop()                     # stack 중에서 시작위치 뽑고
        if S == 99 :                        # 시작위치 99면 성공 (1 출력)
            print(f'#{tc} 1')
            break
        if not visited[S] :
            visited[S] = 1                  # 시작 위치 visited에 저장하고
            for E in range(100) :           # 도착 위치 E 될 수 있는 값 찾아서 stack 저장
                if route[S][E] and not visited[E] :
                    stack.append(E)
        if stack == [] :                    # stack 비었으면 (더이상 갈 데 없음) 0 출력
            print(f'#{tc} 0')
            break
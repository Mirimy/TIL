import sys
sys.stdin = open('input.txt')

for tc in range(1, 11) :
    N = int(input())
    arr = []
    [arr.append(list(map(int, input().split()))) for _ in range(N)]

    # 각 세로줄마다 위에서 아래로 훑으며 N극이 나오면 is_N -> True/ S극이 나오면 교착 +1 하고 is_N 초기화
    is_N = False
    magnetic = 0
    for j in range(N) :
        for i in range(N) :                         # 위에서 아래로 순회하며
            if arr[i][j] == 1 :                     # N극이면 is_N에 표시
                is_N = True
            elif arr[i][j] == 2 and is_N :          # S극이고 is_N (위에 N극 있음)
                magnetic += 1                       # 교착 + 1
                is_N = False                        # is_N 초기화
        is_N = False                                # 다음줄로 넘어갈 때 is_N 초기화
    print(f'#{tc} {magnetic}')
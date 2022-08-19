import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :

    arr = []
    [arr.append(list(map(int, input().split()))) for _ in range(9)]

    num_x = []
    num_y = []
    num_a = []
    result = 1   # 맞는 스도쿠이면 1
    for i in range(9) :
        for j in range(9) :
            # =============== 가로 ====================
            if arr[i][j] not in num_x :
                num_x.append(arr[i][j])
            else :
                result = 0
            # =============== 세로 ====================
            if arr[j][i] not in num_y :
                num_y.append(arr[j][i])
            else :
                result = 0
            # =============== 3x3 구역 ====================
            if i % 3 == 0 and j % 3 == 0 :          # 각 격자의 시작 위치일 때
                for k in range(3) :                 # 그 위치에서 i, j 를 각각 +0, +1, +3 하여 검사
                    for l in range(3) :
                        if arr[i+k][j+l] not in num_a :
                            num_a.append(arr[i+k][j+l])
                        else :
                            result = 0
                num_a = []
        # 다음 줄 넘어가기 전에 초기화
        num_x = []
        num_y = []

    print(f'#{tc} {result}')
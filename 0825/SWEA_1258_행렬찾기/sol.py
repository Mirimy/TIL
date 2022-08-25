import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    finish = [[0] * n for _ in range(n)]                        # arr의 행렬 다 찾았을 때 모습을 finish로 미리 선언
    area = []
    # =================== while문 사용하여 arr가 finish(행렬 모두 찾음) 상태가 될 때까지 수행한다. ==============
    while arr != finish :
        # ====================== 행렬 시작 위치 si, sj 와 가로 길이 width 구하기 ==========
        si = sj = ej  = -1
        for i in range(n) :
            is_start = False
            for j in range(n) :
                if arr[i][j] != 0 and not is_start :
                    si, sj = i, j
                    is_start = True
                elif arr[i][j] == 0 and is_start :
                    ej = j - 1
                    break
            if si != -1 :
                break
        width = ej - sj + 1
        # ================= 행렬 세로 길이 height 구하기 ========================
        height = 0
        for i in range(si, n + 1) :                         # 시작 i 부터 밑으로 가면서
            if arr[i][sj] == 0 :                            # 0 나오면 지금 행렬은 끝난거 -> 탈출!
                break
            height += 1                                     # i 밑으로 옮겨주면서 height + 해서 계산한다
            for j in range(sj, ej + 1) :                    # 찾아놓은 가로길이 (sj ~ ej) 범위에 대해서만 순회
                arr[i][j] = 0                               # 다음에 현재 행렬은 무시하고 찾기 위해 0으로 초기화

        area.append([width, height, width * height])        # width가 열이고 height가 행.. @.@
        # =============== 모든 행렬의 [세로, 가로, 넓이] 를 area 리스트에 저장해 주었다 !! =========
    # ================ while 문 끝 = 있는 행렬 모두 찾음 =========================================


    # =============== area를 1. 크기 순 -> 같다면 2. 행 길이 순으로 정렬해 줄거다 !!( 버블소트 사용 ) ======
    for e in range(len(area) - 1, -1, -1) :
        for i in range(0, e) :
            if area[i][2] > area[i + 1][2] :
                area[i], area[i + 1] = area[i + 1], area[i]
            elif area[i][2] == area[i + 1][2] :
                if area[i][1] > area[i + 1][1] :
                    area[i], area[i + 1] = area[i + 1], area[i]
    # =============== 정렬 완료, 출력해준다 ============================================
    print(f'#{tc} {len(area)}', end='')
    for a in area :
        print(f' {a[1]} {a[0]}', end='')
    print()

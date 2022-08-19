import sys
sys.stdin = open('input.txt')

# 가로 세로 각각 순회하면서 1이면 저장 0 나오면 빠져나와서 len 검사

T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())

    arr = []
    [arr.append(list(map(int, input().split()))) for _ in range(N)]

    puzzle_x = []
    puzzle_y = []
    K_count = 0
    for i in range(N) :
        for j in range(N) :
            # =======================가로=========================
            if arr[i][j] == 1 :                         # 1이면
                puzzle_x.append(j)                      # puzzle 리스트에 저장
                if j == N-1 and len(puzzle_x) == K :    # 맨끝이면 이제 초기화될거니까 그 전에 검사
                    K_count += 1
            else :                                      # 0이면
                if len(puzzle_x) == K :                 # 초기화 하기 전에 앞에 저장한거까지 len 검사하고
                    K_count += 1                        # 맞으면 count 1 추가
                puzzle_x = []                           # 초기화
            # =======================세로=========================
            if arr[j][i] == 1 :
                puzzle_y.append(j)
                if j == N-1 and len(puzzle_y) == K :
                    K_count += 1
            else :
                if len(puzzle_y) == K :
                    K_count += 1
                puzzle_y = []
        # 가로/세로 다음 줄로 넘어가기 전에 초기화
        puzzle_x = []
        puzzle_y = []

    print(f'#{tc} {K_count}')
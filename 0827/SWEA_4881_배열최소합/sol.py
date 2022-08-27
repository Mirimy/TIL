import sys
sys.stdin = open('input.txt')

def select_j(arr, idx, j_idx) : # arr, 0, []
    global Min_sum
    s = 0                       # 일단 지금 j_idx에 있는 것만 더해보기
    for i in range(len(j_idx)):
        s += arr[i][j_idx[i]]
    if idx == N:                # idx 끝까지 진행 됐으면 최솟값인지 판별하여 Min_sum에 저장
        if s < Min_sum :
            Min_sum = s
        return
    else :                      # 가지치기 (idx 끝까지 진행 안됐을 때 합이 Min값보다 높으면 그냥 return)
        if s > Min_sum :
            return

    for j in range(N) :         # j = 0, 1, 2, ... N-1 까지
        if j not in j_idx :     # 이전에 나온 j_idx 에 없는 j에 대해
            select_j(arr, idx + 1, j_idx + [j])    # idx + 1 해주고 j_idx에 지금 선택한 j 값 추가


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Min_sum = 10 * N
    select_j(arr, 0, [])
    print(f'#{tc} {Min_sum}')
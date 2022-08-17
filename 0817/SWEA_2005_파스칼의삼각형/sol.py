import sys
sys.stdin = open('input.txt')

def Pascal(N) :
    if N >= 2 :         # 종료조건 : N이 1보다 작으면 더이상 재귀하지 않는다.
        Pascal(N - 1)   # N-1의 함수 실행하여 memo[N-1]에 저장된 상태

    for i in range(N) :                 # N 길이만큼 순회하며
        if i == 0 or i == N-1 :         # 양 끝은 1 추가
            memo[N-1].append(1)
        else :                          # N열의 [idx]에 들어가는 값 :
                                        # N-1 열에서 [idx-1] + [idx] 더한 값
            memo[N-1].append(memo[N-2][i-1] + memo[N-2][i])


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    memo = []
    [memo.append([]) for _ in range(N)]    # memo => [[], [], [], [], ...]

    Pascal(N)
    print(f'#{tc}')
    for i in memo :
        for j in i :
            print(j, end=' ')
        print()

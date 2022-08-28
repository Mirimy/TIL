import sys
sys.stdin = open('input.txt')

# A 하기 전에 해야할 B 있으면 B 탐색/ ordered에 있으면 탐색x
        # B 하기전에 해야할 일 없으면 ordered에 B 저장
# 1. 해야할 일 없으면 ?
    # order 에 나 저장
# 2. 있으면?
    # 그 일 재귀해서 먼저 해야할 일 먼저 ordered에 저장

def order(S, pre) :
    if S not in ordered :                           # 지금 S 가 ordered에 저장 안되어있고 (=아직 안했고)
        for P in range(1, V + 1) :                  # pre 배열의 S번째 줄 탐색했을 때
            if pre[S][P] and P not in ordered :     # S 하기전에 해야 할 일 P 있고, P 아직 안했으면
                order(P, pre)                       # P로 재귀 (P 전에 해야할 일 찾기)
        ordered.append(S)                           # 나 S 전에 해야할 일 P 모두 해결됐으면 나 S 저장


for tc in range(1, 11) :
    V, E = map(int, input().split())    # V 정점 E 간선
    E_list = list(map(int, input().split()))
    pre = [[0] * (V + 1) for _ in range(V + 1)]
    ordered = []

    for i in range(len(E_list) // 2) :              # i를 하기 전에 처리해야할 j들 -> pre[i][j] == 1
        pre[E_list[2 * i + 1]][E_list[2 * i]] = 1

    for i in range(1, V+1) :                        # 1 ~ V 까지 수에 대해
        order(i, pre)                               # 함수 실행

    print(f'#{tc}', end='')
    for num in ordered :
        print(f' {num}', end='')
    print()




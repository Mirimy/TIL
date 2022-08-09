import sys

sys.stdin = open('input.txt')

# 0번 -> N 번 정류장
# 한 번 충전에 K개 정류장
# 충전기 설치 된 M개 정류장
# 도착할 수 없으면 0 출력
# 최소 몇 번 충전 ?

T = int(input())

for tc in range(T) :

    K, N, M = map(int, input().split())

    M_list = list(map(int, input().split()))
# 충전한 위치 0,1 로 표시한 리스트 M_count
    M_list = [0] + M_list + [N]
    # print(M_list)

    charge = 0
    # 현 충전 상태 S = 풀충전 K
    S = K

    for i in range(len(M_list)) :
        # 일단 감
        if i > 0 :
            S = S - (M_list[i] - M_list[i-1])

        # print(f'i = {M_list[i]} S= {S}')

        # 예외 1. 첫번째 충전소까지 못 갈 때
        if i == 1 and S < 0 :
            charge = 0
            break
        # 예외 2. 마지막 충전소에서 충전 해야할 때
        # if i == (len(M_list) - 1) and (N - M_list[i]) >  K - (M_list[i] - M_list[i-1]) :
        #     charge += 1


        # S 0보다 작으면 저번에 충전했어야함
        if S < 0 :
            charge += 1
            S += K - (S + (M_list[i] - M_list[i-1]))
            if S < 0 :
                charge = 0
                break


        # print(f'Char={charge}, S={S}')

    print(f'#{tc + 1} {charge}')

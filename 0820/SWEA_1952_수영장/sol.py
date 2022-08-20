import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    D, M, MMM, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    fee = [D] * 12

    # ================ 1개월권 가능? ==============
    for i in range(12) :
        if plan[i] * fee[i] > M :
            plan[i] = 1
            fee[i] = M

    # ================ 3개월권 가능? ==============
    can_MMM = {}
    for i in range(10):
        MMM_fee = 0         # i 부터 3개월간 내는 요금
        for m in range(3):
            MMM_fee += plan[i + m] * fee[i + m]
        if MMM_fee > MMM:
            can_MMM[i] = MMM_fee

    # can_MMM {시작위치i : i로부터 3개월간 요금}
    # 에서 가능한 시작위치의 부분집합 뽑아보자
    test_idx = []

    for i1 in can_MMM.keys() :
        test_idx.append([i1])
        for i2 in can_MMM.keys() :
            if i2 != i1 and i2 >= i1 + 3 :
                test_idx.append([i1, i2])
                for i3 in can_MMM.keys() :
                    if i3 != i2 and i3 >= i2 + 3 :
                        test_idx.append([i1, i2, i3])
                        for i4 in can_MMM.keys() :
                            if i4 != i3 and i4 >= i3 + 3 :
                                test_idx.append([i1, i2, i3, i4])

    # 부분집합 중 어느 것이 가장 절약할 수 있는지 찾자
    max_fee = 0
    max_idx = []
    for test in test_idx :
        test_fee = 0
        for idx in test :
            test_fee += can_MMM[idx]
        if test_fee > max_fee :
            max_fee = test_fee
            max_idx = test

    # 정해진 시작위치에서 3개월간은 3개월 요금으로 내자
    for i in max_idx :
        fee[i] = MMM
        fee[i+1] = fee[i+2] = 0
        plan[i] = 1
        plan[i+1] = plan[i+2] = 0

    # ================ 연간 가능? ==============
    f = 0
    for i in range(12) :
        f += fee[i] * plan[i]
    if f > Y :
        fee = [Y] + [0] * 11
        plan = [1] + [0] * 11

    # ================ 결과 계산 ==============
    result = 0
    for i in range(12) :
        result += plan[i] * fee[i]
    print(f'#{tc} {result}')

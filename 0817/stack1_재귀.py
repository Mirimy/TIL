def f(i, N) :       # i : 현재 단계, N : 목표 단계
    if i == N :
        print(i)    # 목표치에서 할 일
        return
    else :
        print(i)    # 일반적으로 각 단계에서 할 일을 적어주는 곳
        f(i+1, N)

f(0, 3)
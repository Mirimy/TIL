import sys
sys.stdin = open('input.txt')

for _ in range(1, 11) :
    tc = int(input())
    num = list(map(int, input().split()))

    target = 0
    minus = 1
    while True :
        num[target] -= minus                # minus 빼주고 그 자리에 저장해놓는다.
        if num[target] <= 0 :               # 조건 : 저장해주려는 값이 0 보다 작아지면 ?
            num[target] = 0                 # 0 저장하고 탈출
            break
        target = (target + 1) % 8           # target 은 ..., 5, 6, 7, 0, 1, 2, ... (0 포함)
        minus = (minus % 5) + 1             # minus 는 1, 2, 3, 4, 5, 1, 2, ... (1부터)

    if num[-1] != 0 :                                       # num 배열 만들었지만 순서 안맞는 경우에는
        result = num[target + 1 :] + num[ : target] + [0]   # 현재 target 번호 뒤부터 읽고, 앞으로 돌아와야 함
    else :                                                  # 순서 맞으면(맨뒤가 0) 그냥 써
        result = num

    print(f'#{tc}', end='')                 # 답 result 출력
    for i in result :
        print(f' {i}', end='')
    print()
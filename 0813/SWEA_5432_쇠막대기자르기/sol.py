import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    arr_str = input()
    arr = arr_str.replace('()','r')    # () 자리에 레이저가 있음을 표시 'r'

    stack = 0    # 지금 위치에서 파이프 몇 개 쌓여있는가?
                # ( 나오면 +1, )나오면 -1
    pipe = 0    # 지금 총 파이프 개수는 몇 개인가? (잘린 것 고려)
    for p in arr :
        if p == '(' :
            stack += 1
            pipe += 1    # 원래 있는 파이프 개수도 카운트
        elif p == ')' :
            stack -= 1
        elif p == 'r' :
            pipe += stack    # 레이저 나오면 지금 파이프 스택만큼 카운트 +

    print(f'#{tc} {pipe}')
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    forth = list(input().split())

    stack = []
    for char in forth :
        # ================ . 나오면 ================
        if char == '.' :
            if stack :
                result = stack.pop()
            else :
                result = 'error'
        # ================ 연산자 나오면 ================
        elif char in '+-*/' :
            if len(stack) >= 2 :        # 스택에 2개는 있어야..
                b = int(stack.pop())
                a = int(stack.pop())
                if char == '+' :
                    stack.append(a + b)
                elif char == '-' :
                    stack.append(a - b)
                elif char == '*' :
                    stack.append(a * b)
                elif char == '/' :
                    stack.append(a // b)
            else :                      # 뽑을 숫자 2개 없으면 error
                result = 'error'
                break
        # ================ 숫자 나오면 ================
        else :
            stack.append(char)
    # =========== 연산 끝난 후 stack에 남아있으면 ===========
    if stack :
        result = 'error'

    print(f'#{tc} {result}')
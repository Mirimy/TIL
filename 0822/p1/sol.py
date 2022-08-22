import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    word = input()
    stack = []
    result = ''

    for char in word :
        if char in '/*+-' :
            stack.append(char)
        else :
            result += char
    for _ in range(len(stack)) :
        result += stack.pop()

    print(f'#{tc} {result}')
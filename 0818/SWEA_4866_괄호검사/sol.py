import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    code = input()

    result = []             # code를 순회하며 result에 쌓는다.
    for c in code :
        if c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']' :   # 괄호 문자에 대해서만 고려
            if result == [] :               # result에 아무것도 없으면 자기자신 추가
                result.append(c)
            elif c == ')' and result[-1] == '(' :       # 내가 닫는 괄호일 때, result의 마지막 원소가 여는 괄호이면
                result.pop()                            # 여는 괄호를 pop 한다.
            elif c == '}' and result[-1] == '{' :
                result.pop()
            elif c == ']' and result[-1] == '[' :
                result.pop()
            else :
                result.append(c)
        else :                          # 괄호 문자가 아닌 것은 pass
            continue

    if result == [] :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')
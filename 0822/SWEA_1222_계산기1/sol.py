import sys
sys.stdin = open('input.txt')

for tc in range(1, 11) :
    N = int(input())
    a = input()

    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # stack에 있을 때
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}  # stack에 들어올 때

    stack = []
    result = ''

    for i in range(len(a)):
        # ============== 연산자일 때 =========================
        if a[i] in isp:
            if stack == []:  # 스택 비었으면 그냥 추가
                stack.append(a[i])
            else:  # 스택에 요소 있으면
                while stack and icp[a[i]] <= isp[stack[-1]]:  # 스택 마지막 요소 isp가 내 icp보다 클때까지
                    result += stack.pop()  # 연산자 pop 해서 출력
                stack.append(a[i])  # 스택[-1] isp가 내 icp보다 크면 push
        # ============== ) 닫는 괄호 일 때 =========================
        elif a[i] == ')':
            while stack[-1] != '(':  # 여는 괄호가 나올 때까지
                result += stack.pop()  # pop해서 출력
            stack.pop()  # 여는 괄호 만난 후 여는 괄호는 버리기
        # ============== 연산자 아닐 때 =========================
        else:
            result += a[i]
            if i == len(a) - 1:
                result += stack.pop()

    for i in result:
        if i not in isp:
            stack.append(i)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if i == '+':
                stack.append(a + b)
            elif i == '*':
                stack.append(a * b)
            elif i == '-':
                stack.append(a - b)
            elif i == '/':
                stack.append(a // b)
    print(f'#{tc} {stack.pop()}')
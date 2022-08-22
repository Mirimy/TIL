a = '3-2*5+4/2-2'
isp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}    # stack에 있을 때
icp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 3}    # stack에 들어올 때

stack = []
result = ''

for i in range(len(a)) :
    # ============== 연산자일 때 =========================
    if a[i] in isp :
        if not stack :                                  # 스택 비었으면 그냥 추가
                stack.append(a[i])
        else :                                            # 스택에 요소 있으면
            while stack and icp[a[i]] <= isp[stack[-1]] : # 스택 마지막 요소 isp가 내 icp보다 클때까지
                result += stack.pop()                     # 연산자 pop 해서 출력
            stack.append(a[i])                            # 스택[-1] isp가 내 icp보다 크면 push
    # ============== ) 닫는 괄호 일 때 =========================
    elif a[i] == ')' :
        while stack and stack[-1] != '(' :                          # 여는 괄호가 나올 때까지
            result += stack.pop()                         # pop해서 출력
        stack.pop()                                       # 여는 괄호 만난 후 여는 괄호는 버리기
    # ============== 연산자 아닐 때 =========================
    else :
        result += a[i]

while stack :
    result += stack.pop()

print(result)

# ===================== 후위표기법 식 계산 ==================

for i in result :
    if i not in isp :               # 연산자 아니면
        stack.append(i)             # stack에 쌓기
    else :                          # 연산자이면
        b = int(stack.pop())        # 스택 top 에서 숫자 두 개 뽑아서 연산
        a = int(stack.pop())
        if i == '+' :
            stack.append(a+b)
        elif i == '*' :
            stack.append(a*b)
        elif i == '-' :
            stack.append(a-b)
        elif i == '/' :
            stack.append(a//b)
print(stack.pop())
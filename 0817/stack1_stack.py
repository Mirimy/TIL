# stackSize * [0] 으로 구현
stackSize = 10
stack = [0] * stackSize
top = -1

top += 1         # 탑 증가
stack[top] = 1   # 스택에 push

top += 1         # push(2)
stack[top] = 2

top -= 1         # pop(1)
temp = stack[top + 1]
print(temp)

temp = stack[top]       # pop(2)
top -= 1
print(temp)

# append, pop으로 구현
stack2 = []
stack2.append(10)       # push
stack2.append(20)
print(stack2.pop())     # pop
print(stack2.pop())
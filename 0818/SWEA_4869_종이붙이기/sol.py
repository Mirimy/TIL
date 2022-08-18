import sys
sys.stdin = open('input.txt')
def factorial(n) :
    if n > 1 :
        return n * factorial(n-1)
    else :
        return 1


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    N = N // 10

    result = 0

    for two in range(N // 2 + 1):   # 2칸짜리의 개수 기준
        one = N - (two * 2)         # 1칸 : one 개, 2칸 : two 개
        result += int(factorial(one + two) / (factorial(one) * factorial(two))) * 2**(two)
        # one + two 개를 줄세우는 경우의 수 ( 순열 조합,...? 그거..)
        # 2칸짜리는 가로로 나눌 수 있으므로 2**(two) 해준다
    print(f'#{tc} {result}')
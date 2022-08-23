import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    print(f'#{tc}')
    print(N // 50000, end=' ')
    N %= 50000
    print(N // 10000, end=' ')
    N %= 10000
    print(N // 5000, end=' ')
    N %= 5000
    print(N // 1000, end=' ')
    N %= 1000
    print(N // 500, end=' ')
    N %= 500
    print(N // 100, end=' ')
    N %= 100
    print(N // 50, end=' ')
    N %= 50
    print(N // 10)
    N %= 10


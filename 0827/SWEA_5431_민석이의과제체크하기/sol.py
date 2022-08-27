import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))

    not_submit = ''
    for i in range(1, N+1) :
        if i not in submit :
            not_submit += ' '  + str(i)

    print(f'#{tc}{not_submit}')
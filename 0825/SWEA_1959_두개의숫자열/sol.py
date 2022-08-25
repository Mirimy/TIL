import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))     # N개
    B = list(map(int, input().split()))     # M개

    if len(A) > len(B) :
        A, B = B, A

    max_s = 0
    for st in range(0, len(B) - len(A) + 1) :
        num_s = 0
        for i in range(len(A)):
            num_s += A[i] * B[st + i]
        if num_s > max_s :
            max_s = num_s

    print(f'#{tc} {max_s}')

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())            # K개 선택
    score = list(map(int, input().split()))     # N개 점수

    max_s = 0
    for subset in range(1<<N) :
        s = 0
        if bin(subset)[2:].count('1') == K:
            for i in range(N) :
                if subset & (1<<i) :
                    s += score[i]
            if s > max_s :
                max_s = s

    print(f'#{tc} {max_s}')
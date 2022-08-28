import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())            # K개 선택
    score = list(map(int, input().split()))     # N개 점수

    for end in range(N - 1 , N - K - 1, -1) :       # 2, 0,-1
        for i in range(0, end) :
            if score[i] > score[i + 1] :
                score[i], score[i + 1] = score[i + 1], score[i]
    s = 0
    for i in range(K) :
        s += score[N - i - 1]

    print(f'#{tc} {s}')
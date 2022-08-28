import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M, K = map(int, input().split())     # N명 M초 K개
    cstm = list(map(int, input().split()))   # N 명 도착 시간 초
    cstm.sort()

    result = 'Possible'
    pre = 0
    bung = 0
    before_s = 0
    for s in cstm :
        bung += ((pre + (s - before_s)) // M) * K
        bung -= 1
        pre = (pre + (s - before_s)) % M
        if bung < 0:
            result = 'Impossible'
        before_s = s
    print(f'#{tc} {result}')
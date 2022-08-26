import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())

    nums = list(map(int, input().split()))

    first = (1 + M) % N         # 첫번째로 올 숫자의 위치
    result = nums[first - 1]    # idx니까 -1
    print(f'#{tc} {result}')
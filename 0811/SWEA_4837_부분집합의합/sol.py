import sys

sys.stdin = open('input.txt')

# N 개의 원소를 갖고 합이 K 인 부분집합의 개수

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())
    cnt = 0

    # 길이가 12인 배열의 부분집합 전체 경우의 수 생성
    for i in range(1, 1<<12) :
        result = 0

        # 생성된 2진수 i의 문자열에 1의 개수 = 부분집합의 개수 = N개
        if str(bin(i)[2:]).count('1') == N :

            # (1,0,0) , (0,1,0), (0,0,1) 이런식으로 원소 하나만 뽑는 부분집합
            for j in range(12):
                # 위 원소가 부분집합 i 에 포함됐다면 배열에서 해당하는 수 (j+1)을 합산
                if i & (1 << j):
                    result += j + 1
        # 부분집합 i 의 모든 원소를 더한 값이 K 이면 개수 count +1 해준다
        if result == K :
            cnt += 1

    print(f'#{tc} {cnt}')

import sys

sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1) :
    arr = list(map(int, input().split()))
    N = len(arr)

    for i in range(1<<N) :
        # 모든 경우의 수 구할건데
        # 각 경우의 수로 만들어지는 부분집합들의
        # 합이 0이 되는 순간이 있는지 확인 할 것.
        result = 0

        # 내가 가진 각 요소들을 부분집합에
        for j in range(N) :
            # 포함시킬거냐 말거냐를 판단해야한다
            # i == i 번째 경우의 수
            # j == arr[j] 번째 요소를 넣을거냐 말거냐
            if i & (1<<j) :   # True 나오면
                result += arr[j]

        if result == 0:
            print(f'#{tc} {True}')
            break
    else :
        print(f'#{tc} {False}')
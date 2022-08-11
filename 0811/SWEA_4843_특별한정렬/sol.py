import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    nums = list(map(int, input().split()))

    result = []
    # result 리스트 길이가 10보다 작을 때 실행
    while len(result) < 10 :
        max_num = nums[0]
        min_num = nums[0]
        # 입력받은 숫자 배열에서 최대, 최소 값 찾기
        for i in nums :
            if i > max_num :
                max_num = i
            if i < min_num :
                min_num = i
        # result 리스트에 최대, 최소 순으로 추가
        result.append(max_num)
        result.append(min_num)
        # result에 추가한 요소는 입력받은 배열에서 지움
        nums.remove(max_num)
        nums.remove(min_num)

    print(f'#{tc}', end=' ')
    for i in result :
        print(i, end=' ')
    print()

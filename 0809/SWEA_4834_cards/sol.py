import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T) :
    N = int(input())
    a = input()

# count list 만들어서 입력 숫자 정보 저장
    count_lst = [0] * 10
    for num in a :
        count_lst[int(num)] += 1

# count list 중 max 값 찾기
    max_count = 0
    max_count_num = 0
    for i in range(len(count_lst)) :
        # 큰 수가 max_count랑 같을 때 덮어쓰려면 >=
        if count_lst[i] >= max_count :
            max_count = count_lst[i]
            max_count_num = i

    print(f'#{tc + 1} {max_count_num} {max_count}')
import sys
sys.stdin =  open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[0]
    max_idx = -1
    start_idx = 0
    num = 0
    budget = 0

    while start_idx < len(price) :
        for idx in range(start_idx, len(price)) :    # 저번 범위 다음 ~ 끝까지
            if price[idx] > max_price :    # max price의 idx 찾기
                max_price = price[idx]
                max_idx = idx

        for idx in range(start_idx, len(price)) :    # 저번 범위 다음 ~ 끝까지
            if price[idx] == max_price :    # 순회하며 max price 나오면 팔고
                budget += price[idx] * num  # 비교값들 초기화
                num = 0
                start_idx = idx + 1
                max_price = 0
                break
            else :
                budget -= price[idx]    # max price 아니면 사재기
                num += 1

    print(f'#{tc} {budget}')
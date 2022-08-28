import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    nums = list(map(int, input().split()))

# 단조 증가하는 수 ? => 감소하지 않는 수열

    max_danjo = -1
    for i in range(N) :
        for j in range(N) :
            if i != j :
                num = str(nums[i] * nums[j])

                is_danjo = True
                for k in range(len(num) - 1) :
                    if int(num[k]) > int(num[k + 1]) :
                        is_danjo = False
                        break

                if is_danjo and int(num) > max_danjo :
                    max_danjo = int(num)


    print(f'#{tc} {max_danjo}')
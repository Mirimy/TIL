import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    max_cnt = 0
    for a in str1 :
        a_cnt = 0
        for b in str2 :
            if a == b :
                a_cnt += 1

        if a_cnt > max_cnt :
            max_cnt = a_cnt

    print(f'#{tc} {max_cnt}')
import sys

sys.stdin =  open('input.txt')

N = int(input())

for tc in range(N) :
    random_num = str(input())
    count_list = [0] * 10

    for num in random_num :
        count_list[int(num)] += 1


    tri = run = 0
    for i in range(10) :

        while (count_list[i] >= 1 and count_list[i+1] >= 1 and count_list[i+2] >=1) and (i < 8):
                run += 1
                count_list[i] -= 1
                count_list[i+1] -= 1
                count_list[i+2] -= 1
        while count_list[i] >= 3 :
            tri += 1
            count_list[i] -= 3


    if tri + run == 2 :
        print(f'#{tc + 1} 1')
    else :
        print(f'#{tc + 1} 0')

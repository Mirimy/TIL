import sys
sys.stdin = open('input.txt')

nums = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4,
       'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

T = int(input())

for tc in range(1, T+1) :
    N = int(list(input().split())[1])
    str_arr = list(input().split())

    result = []

    for i in range(10) :
        for arr_num in str_arr :
            if nums[arr_num] == i :
                result.append(arr_num)

    print(f'#{tc}')
    for i in range(len(result)) :
        print(result[i], end=' ')

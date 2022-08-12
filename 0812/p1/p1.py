# 문자열 뒤집기

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    word = input()

    # 슬라이싱
    print(f'#{tc} {word[::-1]}')

    # reversed 내장 함수
    result = list(reversed(word))
    # list -> str
    print(f'#{tc} {"".join(result)}')

    # 뒤에서부터 저장
    result = ''
    for idx in range(len(word)-1, -1, -1) :
        result += word[idx]
    print(f'#{tc} {result}')

    #
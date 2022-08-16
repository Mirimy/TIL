import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    char, key = input().split()

    # 문자열 char 내에서 key의 개수 count
    cnt = 0
    i = 0
    while i <= len(char) - len(key) :   # 시작위치
                                    # while 쓴 이유 ? key 나왔을때 idx 건너뛰려고
        is_same = True
        for j in range(len(key)) :  # 시작위치로부터 몇개?
            if char[i+j] != key[j] :
                is_same = False    # 하나라도 다르면 False
                i += 1      # key 아니면 다음 idx 조사
                break
        if is_same :     # is_same 모두 같으면 => True이면
            cnt += 1    # count 1 추가
            i += len(key)    # key 길이만큼 idx 건너뛰기

    # 원래 글자 길이 - (키 길이 * 키 개수) + (1 * 키 개수)
    result = len(char) - (cnt * len(key)) + cnt
    print(f'#{tc} {result}')
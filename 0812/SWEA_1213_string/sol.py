import sys
sys.stdin = open('input.txt', encoding='utf-8')

for _ in range(10) :
    tc = int(input())
    ptn = input()
    tgt = input()
    count = 0

    # target 문자열에서 idx 1씩 추가해가며 pattern 문자열 길이만큼 빈 문자열 char에 저장
    for start_i in range(len(tgt) - len(ptn) + 1) :
        char = ''
        for i in range(start_i, start_i + len(ptn)) :
            char += tgt[i]

        # 저장된 char 이 pattern 값과 같으면 count 1 추가
        if char == ptn :
            count += 1

    print(f'#{tc} {count}')
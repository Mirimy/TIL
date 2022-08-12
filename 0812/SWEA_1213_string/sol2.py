import sys
sys.stdin = open('input.txt', encoding='utf-8')

for _ in range(10) :
    tc = int(input())
    ptn = input()
    tgt = input()
    count = 0

    # target 문자열에서 idx 1씩 추가해가며 pattern 문자열 길이만큼 빈 문자열 char에 저장
    for start_i in range(len(tgt) - len(ptn) + 1) :
        # 찾고 싶은 pattern 의 첫 문자와 일치하는 target 시작위치 찾기
        if tgt[start_i] == ptn[0] :
            i = 1
            is_same = True

            # 시작위치에서 뒤로 pattern의 길이만큼 탐색해서 틀린 부분 있으면 False 저장
            while i <= len(ptn) - 1 :
                if tgt[start_i + i] != ptn[i] :
                    is_same = False
                i += 1
        # 첫 문자 일치하지 않으면 False 저장
        else :
            is_same = False
        # 값 True 이면 일치 -> 카운트 1 +
        if is_same :
            count += 1


    print(f'#{tc} {count}')
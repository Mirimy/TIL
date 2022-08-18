import sys
sys.stdin = open('input.txt')

for tc in range(1, 11) :
    N, char = input().split()
    N = int(N)

    pw = []                         # 빈 문자열 pw 만들기
    for i in range(len(char)) :     # 입력 문자열 순회하며
        if i == 0 or pw == []:      # 처음 원소거나 pw에 비교대상 없으면
            pw.append(char[i])      # 문자 저장
        elif char[i] == pw[-1] :    # pw 마지막 원소와 같으면
            pw.pop()                # 저장하지 않고 마지막 원소 빼내기
        else :                      # pw 마지막 원소와 다르면
            pw.append(char[i])      # 문자 저장

    print(f'#{tc} {"".join(pw)}')
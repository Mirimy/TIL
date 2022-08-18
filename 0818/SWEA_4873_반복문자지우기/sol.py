import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    char = input()

    result = []
    for i in range(len(char)) :     # result []에 char 차례로 추가하면서 검사
        if result == []:            # result에 아무것도 없으면 검사 x 그냥 문자 추가
            result.append(char[i])
        elif char[i] == result[-1] :    # result의 마지막 원소와 같으면 추가 안 하고
            result.pop()                # 마지막 원소 빼냄 (pop)
        else :
            result.append(char[i])      # 마지막 원소랑 같지 않으면 그냥 추가

    len_result = len(result)
    print(f'#{tc} {len_result}')
    print(result)
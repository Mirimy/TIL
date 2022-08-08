import sys

# question.py 실행시 파일 읽어옴
sys.stdin = open('input.txt')

# 전체 text case 수 N개
N = int(input())
# ctrl + shift + F10 : 현재 포커싱 파일 실행

# N 번 만큼 입력받을 a들을 각각 입력받아서
# 각 상황에 맞는 출력 결과를 만들어야 한다.

for tc in range(N):
    a = int(input())

    if a % 2 :
        result = '홀수'
    else:
        result = '짝수'

    print(f'#{tc + 1 } {result}')
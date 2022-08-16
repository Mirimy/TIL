import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    char, key = input().split()

    result = len(char.replace(key, 'a'))
    print(f'#{tc} {result}')
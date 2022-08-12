# int to ASKII

def itoa(num) :
    char = ''
    n = abs(num)
    # 넘겨받은 정수를 0이 되기 전까지 계속 반복
    if n == 0 :
        return chr(48)

    # 일의자리 수부터 끊어서 문자열로 변환 // ord('0') == 48
    while n != 0 :
        char = chr((n % 10) + 48) + char
        n = n // 10

    # 만약 처음 넘겨 받은 값이 음수였다면 문자열 앞에 '-'를 붙여서 반환한다.
    if num < 0 :
        char = '-' + char

    return char

print(itoa(123))
print(itoa(0))
print(itoa(-123))
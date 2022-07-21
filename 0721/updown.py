import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    # print(answer)

    num = int(input('1 이상 10000 이하의 숫자를 입력하세요. : '))
    

    while num != answer :
        if num < 1 or num > 10000 :
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.\n')
        elif num < answer :
            print('Up!!!\n')
            counts += 1
        elif num > answer :
            print('Down!!!\n')
            counts += 1
        num = int(input('1 이상 10000 이하의 숫자를 입력하세요. : '))

    counts += 1
    print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.\n')
    regame = input('게임을 재시작 하시려면 y, 종료하시러면 n을 입력하세요. : ')

    if regame == 'y' :
        is_playing = True
    elif regame == 'n' :
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
        is_playing = False
    else :
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
        is_playing = False
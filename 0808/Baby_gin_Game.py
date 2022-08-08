# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는
# 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경오를 triplet 이라고 한다.
# 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin 으로 부른다.
# 6자리 숫자를 입력받아 Baby-gin 여부를 찾아라
#
# 완전 검색
# 모든 경우의 수를 테스트한 후 최종 해법을 도출하는 방법
# 주어진 6개의 숫자로 만들 수 있는 모든 수열 만든 후 앞 3/ 뒤 3자리 잘라 테스트
#
# 완전 검색이 아닌 방법
# counts 배열로 나타내여 1 1 1 / 3 등 으로 찾아보자.

num = 456789
c = [0] * 12    # 개수 누적할 리스트

# 1의 자리 카운트 저장하고 날리기 반복해서 카운트 배열 c 만들기
for i in range(6) :
    c[num % 10] += 1
    num //= 10

#
    i = 0
    tri = run = 0
    while i < 10 :
        if c[i] >= 3 :
            c[i] -= 3
            tri += 1
            continue;  # i 자리에서 triplet 찾으면 while로 돌아가서 그 자리에서 run까지 조사

        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 :
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue;
        i += 1

    if run + tri == 2 :
        print('Baby Gin')
    else :
        print('Lose')
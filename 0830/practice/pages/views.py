from django.shortcuts import render
import random
import requests

# Create your views here.
def lotto(request) :
    # lotto 당첨 번호 가져오기
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    response = requests.get(URL).json()
    win = []
    for i in range(1, 7) :
        win.append(response.get(f'drwtNo{i}'))
    bonus = response.get('bnusNo')

    rank = [0] * 6
    # 무작위 lotto 번호 1000번 뽑기
    for _ in range(1000) :
        lotto = []
        while len(lotto) < 6 :
            num = random.randint(1, 45)
            if num not in lotto :
                lotto.append(num)
        # 당첨 판별하여 rank에 저장
        counts = 0
        is_bonus = False
        for n in lotto :
            if n in win :
                counts += 1
            elif n == bonus :
                is_bonus = True
        
        if counts == 6 :
            rank[0] += 1
        elif counts == 5 and is_bonus :
            rank[1] += 1
        elif counts == 5 and not is_bonus :
            rank[2] += 1
        elif counts == 4 :
            rank[3] += 1
        elif counts == 3 :
            rank[4] += 1
        else :
            rank[5] += 1

    # lotto.html 로 넘겨줄 data들        
    context = {
        'win' : win,
        'bonus' : bonus,
        'rank' : rank
    }
    return render(request, 'lotto.html', context)
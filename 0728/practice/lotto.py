# 여기에 필요한 모듈을 추가합니다.
import random
import json


class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []
#  self.number_lines = [] 로또 번호에 해당하는 모든 줄을 담는 용도

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        # self.number_lines = []
        for i in range(n) :
            lotto_numbers = random.sample(range(1, 46) , 6)
            lotto_numbers.sort()
            self.number_lines.append(lotto_numbers)
# 반환값 없음. test용 print
#        print(self.number_lines)
# line_numbers = [[로또번호1], [로또번호2], ... 6개]
        
        '''
        # 방법 2. 리스트 컴프리헨션
        [표현식] => [ num for num in range(10)]
        [표현식 결과]=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 이걸 a에 담기
        a = num for num in range(10)
        line_numbers = [sorted(list(random.sample(range(1, 46), 6))) for _ in range(n)]

        return line_numbers
        '''
        

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = Lotto.get_draw_date(draw_number)
        print('===========================================')
        print(f'             제 {draw_number} 회 로또')
        print('===========================================')
        print(f'추첨일 : {year}/{month}/{day} (토)')
        print('===========================================')

        counts = 0
        while counts < len(self.number_lines) :
            if counts == 0 :
                print(f'A : {self.number_lines[0]}')
            elif counts == 1 :
                print(f'B : {self.number_lines[1]}')
            elif counts == 2 :
                print(f'C : {self.number_lines[2]}')
            elif counts == 3 :
                print(f'D : {self.number_lines[3]}')
            elif counts == 4 :
                print(f'E : {self.number_lines[4]}')
            counts += 1
# 반환값 없음.



    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = Lotto.get_lotto_numbers(draw_number)
        
        print('===========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('===========================================')

        for i in range(len(self.number_lines)) :
            same_main_counts, is_bonus = Lotto.get_same_info(main_numbers, bonus_number, self.number_lines[i])
            rank = Lotto.get_ranking(same_main_counts, is_bonus)

            if i == 0 :
                s = 'A'
            elif i == 1 :
                s = 'B'
            elif i == 2 :
                s = 'C'
            elif i == 3 :
                s = 'D'
            elif i == 4 :
                s = 'E'

            if is_bonus == True :
                bs = ' + 보너스'
            else :
                bs = ''
            
            if rank == -1 :
                print(f'{s} : {same_main_counts}개{bs} 일치 (낙첨)')
            elif rank == 5 :
                print(f'{s} : {same_main_counts}개{bs} 일치 (5등 당첨!)')
            elif rank == 4 :
                print(f'{s} : {same_main_counts}개{bs} 일치 (4등 당첨!)')
            elif rank == 3 :
                print(f'{s} : {same_main_counts}개{bs} 일치 (3등 당첨!)')
            elif rank == 2 :
                print(f'{s} : {same_main_counts}개{bs} 일치 (2등 당첨!)')
            elif rank == 1 :
                print(f'{s} : {same_main_counts}개{bs} 일치 (1등 당첨!)')


# 각각 line 번호랑 당첨번호랑 맞춰서 (맞는개수)
# 반환값 없음



    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        draw_num = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        draw_detail = json.load(draw_num)
# draw_detail 은 딕셔너리
# "drwNoDate": "2022-07-09"
        year = draw_detail['drwNoDate'][:4]
        month = draw_detail['drwNoDate'][5:7]
        day = draw_detail['drwNoDate'][-2:]

        return year, month, day

        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        draw_num = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        draw_detail = json.load(draw_num)

        main_numbers = [draw_detail['drwtNo1'],draw_detail['drwtNo2'],draw_detail['drwtNo3'],draw_detail['drwtNo4'],draw_detail['drwtNo5'],draw_detail['drwtNo6']]
        bonus_number = draw_detail['bnusNo']

        return main_numbers, bonus_number
# "drwtNo1": 10
# return main_numbers(메인번호 리스트) [ 1, 2, 3, 4, 5, 6]
# bonus_number(보너스 번호) = 13

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
# 'lotto.get_same_info(mains, bonus, [10, 14, 16, 18, 29, 35]) == (6, False)'
        same_main_counts = 0
        for mnum in main_numbers :
            for lnum in line :
                if mnum == lnum :
                    same_main_counts += 1
        is_bonus = False
        for lnum in line :
            if bonus_number == lnum :
                is_bonus = True

        return same_main_counts, is_bonus
# return same_main_counts(로또번호 한줄, 메인번호 일치숫자), is_bonus(보너스일치여부)

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus): 
        if same_main_counts == 6 :
            ranking = 1
        elif same_main_counts == 5 and is_bonus == True :
            ranking = 2
        elif same_main_counts == 5  and is_bonus == False :
            ranking = 3
        elif same_main_counts == 4 :
            ranking = 4
        elif same_main_counts == 3 :
            ranking = 5
        else :
            ranking = -1
        return ranking

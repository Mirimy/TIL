# wiki 폴더의 pokemon 파일에 있는 Pokemon 클래스를 가져오기
from wiki.pokemon import Pokemon

class Pikachu(Pokemon) :    # Pokemon 클래스 상속받기 -> (Pokemon)
    no = 25    # Pikachu만 갖는 속성 변수

    def __init__(self, name='피카츄', lv=5) :
        # 내 직속 상속 부모가 가진 메서드 호출하기 .__init__
        # 호출할 때, 부모 클래스에 필요한 인자 넘겨주기 (name, lv)
        # Pokemon 클래스의 def init 을 한 번 실행시킨다.
        super().__init__(name, lv)
        # 부모 init 호출한 다음에 세부 사항 수정할 수 있음 (오버라이드)
        self.skill = '전기 충격'
        
    def attack(self):
        return '찌릿 찌릿'

    def walk(self):
        return '뚜벅 뚜벅'
        

class Metamong(Pokemon) :
    no = 132

    def __init__(self, name, lv=1):
        super().__init__(name, lv)
        self.skill = '변신'

    def attack(self):
        return '메타 메타'
    
    def eat(self) :
        return '냠냠'

pika = Pikachu()    
# pika는 Pikachu 클래스의 인스턴스이자, 상속받은 Pokemon 클래스의 인스턴스이다.
print(pika.info)
print(pika.walk())
print(Pikachu.bell_population)

meta = Metamong('메타몽')
print(meta.info)
print(Metamong.bell_population)




# Pikachu 와 Metamong 클래스 가져와서 자식 클래스 만들기
class Child(Pikachu, Metamong) :    
    pass

ch = Child('메타몽')
print(ch.skill)     # '전기 충격' / 왜냐면 Pikachu를 우선 상속해서
print(ch.eat())     # '냠냠' / Pikachu에 없는 Metamong의 값은 상속
print(Pikachu.bell_population)  # 0
print(Metamong.bell_population) # 0
print(Child.bell_population)    # 1




# 우선순위 잘 설정해주면 Metamong을 상속받음
class Brother(Metamong, Pikachu) :
    pass

br = Brother('메타몽')
print(br.skill)   
print(br.eat())     

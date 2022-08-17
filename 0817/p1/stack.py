# class 베이스 stack 구현
class Stack :

    # stack이 최초 생성될 때 필요한 정보들
    # 생성자에 담을건데
    # stack이라는 자료형은 최대 크기가 지정되어야 함
    def __init__(self, size):
        # stack의 크기
        self.size = size
        # stack에 자료를 저장할 구조
        # stack 처음 만들어질 때, 각 요소들은 값이 없어야 한다. (0 X None o)
        self.arr = [None] * size
        # stack의 최상단
        self.top = -1

    # stack이 비어있는지 확인하는 메서드
    def is_empty(self):
        if self.top == -1 :
            return True
        else :
            return False
    # stack이 가득 찼는지 확인하는 메서드
    def is_full(self):
        if self.top + 1 == self.size :
            return True
        else:
            return False
    # stack에 값을 추가하는 연산
    def push(self, item):
        if self.is_full() :
            raise Exception('stack이 가득 찼습니다.')    # 오류 예외처리
        else :
            self.top += 1
            self.arr[self.top] = item
    # stack에 값을 제거하는 연산
    def pop(self):
        if self.is_empty() :
            raise Exception('stack이 비었습니다.')
        else :
            value = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return value
a = Stack(3)
print(a.arr)
print(a.top)
print(a.is_empty())
print()
a.push('A')
print(a.arr)
print(a.top)
print(a.is_empty())
print()
a.push('B')
print(a.arr)
print(a.top)
print(a.is_empty())
print()
a.push('C')
print(a.arr)
print(a.top)
print(a.is_empty())
print(a.is_full())
print()
print(a.pop())
print(a.arr)
print(a.top)
print()
print(a.pop())
print(a.arr)
print(a.top)
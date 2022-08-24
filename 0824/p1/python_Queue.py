class Queue :

    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = -1
        self.front = -1

    def enQueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    def deQueue(self):
        self.front += 1
        return self.items[self.front]



q = Queue(5)
print(q.items)

q.enQueue('A')      # enQueue('A')
q.enQueue('B')      # enQueue('B')
print(q.items)
print('=' * 30)
print(q.deQueue())  # deQueue()
print(q.items)      # front만 한 칸 뒤로 이동 (큐 데이터 삭제는 아님)
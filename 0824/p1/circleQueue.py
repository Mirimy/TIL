class Queue :

    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = 0
        self.front = 0

    def enQueue(self, item):
        if self.isFull() :
            print('is Full')
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = item

    def deQueue(self):
        self.front = (self.front + 1) % self.size
        return self.items[self.front]

    def isFull(self):
        return self.front == (self.rear + 1) % self.size



q = Queue(5)
print(q.items)

q.enQueue('A')      # enQueue('A')
print(q.rear, q.front)
q.enQueue('B')      # enQueue('B')
print(q.rear, q.front)
q.enQueue('C')      # enQueue('C')
print(q.rear, q.front)
q.enQueue('D')      # enQueue('D')
print(q.rear, q.front)
q.enQueue('E')      # enQueue('E')
print(q.rear, q.front)
print(q.items)
print('=' * 30)
print(q.deQueue())  # deQueue()
print(q.items)      # front만 한 칸 뒤로 이동 (큐 데이터 삭제는 아님)
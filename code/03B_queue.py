# %%
class Queue:
    def __init__(self, size=100005):
        self.size = size
        self.q = [None] * self.size
        self.head = 1
        self.tail = 1

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, obj):
        self.q[self.tail] = obj
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.size - 1:
            self.head = 0
            return self.q[self.size - 1]
        else:
            self.head += 1
            return self.q[self.head - 1]


qu = Queue()

li = list(map(int, input().split()))
n = li[0]
q = li[1]

for i in range(n):
    li = list(map(str, input().split()))
    li[1] = int(li[1])
    qu.enqueue(li)

# q = 100
# qu.enqueue(['p1', 150])
# qu.enqueue(['p2', 80])
# qu.enqueue(['p3', 200])
# qu.enqueue(['p4', 350])
# qu.enqueue(['p5', 20])

time = 0
while True:
    temp_list = qu.dequeue()
    temp_name = temp_list[0]
    temp_num = temp_list[1]
    if temp_num <= q:
        time += temp_num
        print(temp_name + ' {}'.format(time))
        if qu.is_empty():
            break
    else:
        li = [temp_name, temp_num - q]
        qu.enqueue(li)
        time += q

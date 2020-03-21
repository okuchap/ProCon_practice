# %%
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.tail = 0

    def push(self, new):
        self.stack[self.tail] = new
        self.tail += 1

    def pop(self):
        self.tail -= 1
        return self.stack[self.tail]


max_size = 105

# li = list(map(str, input().split()))
li = ['1', '2', '+', '3', '4', '-', '*']
N = len(li)
stack = Stack(max_size)

for i in range(N):
    ch = li[i]
    if ch in ['+', '-', '*']:
        num_2 = stack.pop()
        num_1 = stack.pop()
        if ch == '+':
            stack.push(num_1 + num_2)
        elif ch == '-':
            stack.push(num_1 - num_2)
        else:
            stack.push(num_1 * num_2)
    else:
        stack.push(int(ch))

print('{}'.format(stack.stack[0]))


# %%

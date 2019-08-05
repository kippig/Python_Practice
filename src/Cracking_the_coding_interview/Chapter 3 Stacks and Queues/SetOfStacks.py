from Stack import Stack


class SetOfStacks:

    def __init__(self, capacity=3):
        self.stacks = [Stack()]
        self.capacity = capacity

    def __len__(self):
        return sum(map(len, self.stacks))

    def pop(self):
        l = len(self.stacks[-1])
        if l == 0:
            return None
        else:
            value = self.stacks[-1].pop()
            if l == 1:  # stack is now empty
                self.stacks.pop()
            return value

    def push(self, value):
        l = len(self.stacks[-1])
        if l == self.capacity:
            self.stacks.append(Stack())
            self.stacks[-1].push(value)
        else:
            self.stacks[-1].push(value)

    def pop_at(self, k):
        return self.stacks[k].pop()

    def __repr__(self):
        s = ''.join(map(lambda x: str(x) + '\n', self.stacks))
        return s


s = SetOfStacks()
bob = range(10)
for x in bob:
    s.push(x)
print(s)



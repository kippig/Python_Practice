from Cons import Cons


class Stack:
    # Cons Based Stack

    def __init__(self):
        self.length = 0
        self.body = None
        self.min = None

    def __len__(self):
        return self.length

    def pop(self):
        if self.length > 0:
            val, self.body, self.length = self.body.head, self.body.tail, self.length - 1
            return val
        return None

    def push(self, value):
        self.body = Cons(value, self.body)
        self.length += 1
        if self.min is None or value <= self.min:
            self.min = value

    def peek(self):
        return self.body.head

    def is_empty(self):
        return self.length == 0

    def min(self):
        return self.min

    def __repr__(self):
        return '{}'.format(self.body.__repr__())

    def __str__(self):
        return '{}'.format(self.body.__repr__())

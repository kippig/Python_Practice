class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        if len(arr) == 0:
            return None
        else:
            return cls(arr[0], Cons.from_array(arr[1:]))

    def filter(self, fn):

        def helper(algebraic_list, fn):
            if algebraic_list is None:
                return None

            filtered = not fn(algebraic_list.head)
            if not filtered:
                return Cons(algebraic_list.head, helper(algebraic_list.tail, fn))
            elif filtered:
                return helper(algebraic_list.tail, fn)

        return helper(self, fn)

    def map(self, fn):

        def helper(algebraic_list, fn):
            if algebraic_list is None:
                return None
            else:
                return Cons(fn(algebraic_list.head), helper(algebraic_list.tail, fn))

        return helper(self, fn)

    def leaf(self):
        if self.tail is None:
            return self.tail
        else:
            return self.tail.leaf()

    def reverse(self):
        r = None
        p1 = self
        while p1 is not None:
            r = Cons(p1.head, r)
            p1 = p1.tail
        return r

    def equals(self, other):
        if self.tail is None and other.tail is None:
            return True
        elif self.tail is None or other.tail is None:
            return False
        elif self.head == other.head:
            return self.tail.equals(other.tail)
        else:
            return False

    def __len__(self):
        if self.tail is None:
            return 1
        else:
            return len(self.tail) + 1

    def drop(self, num):
        for i in range(num):
            if self.tail is None:
                return None
            else:
                self = self.tail
        return self

    def __repr__(self):
        return "List{}".format(self.to_array())
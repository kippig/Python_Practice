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

    def __repr__(self):
        return "List{}".format(self.to_array())

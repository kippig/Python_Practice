import random


class BST:

    def __init__(self, value, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.size = 1

    def insert(self, value):
        if value > self.value:
            if self.rchild is None:
                self.rchild = BST(value=value)
            else:
                self.rchild.insert(value)
        elif value < self.value:
            if self.lchild is None:
                self.lchild = BST(value=value)
            else:
                self.lchild.insert(value)
            self.size += 1
        else:
            self.size += 1

    def children(self):
        return self.lchild, self.rchild

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children():
            if child is not None:
                ret += child.__repr__(level+1)
        return ret

    def find(self, value):
        if self.value == value:
            return self.size
        if (value < self.value or self.rchild is None) and self.lchild is not None:
            return self.lchild.find(value)
        elif (value > self.value or self.lchild is None) and self.rchild is not None:
            child_size = self.rchild.find(value)
            if child_size is not None:
                return child_size + self.size
            return child_size
        else:
            return None

    def rank(self, value):
        v = self.find(value)
        if v is not None:
            return v - 1
        return None


def rank_from_stream(stream, steps, tree=None):
    if tree is None:
        value_tree = BST(next(stream))
        steps -= 1
    else:
        value_tree = tree
    for i in range(steps):
        value_tree.insert(next(stream))
    return value_tree


def rando(n):
    while True:
        yield random.randint(0, n)


def arr_stream():
    arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    for item in arr:
        yield item

#tree = rank_from_stream(rando(100), 5)
tree = rank_from_stream(arr_stream(), 9)
print(tree)
print(tree.rank(1))
print(tree.rank(3))
print(tree.rank(4))




import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Graph import Tree, BST
from datetime import datetime


# this could be optimised with dynamic programming
def choose_iter(elements, length):
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next


def choose(l, k):
    return list(choose_iter(l, k))


def mix_seqs(s1, s2):
    length = len(s1) + len(s2)
    if length == 0:
        return [[]]

    if len(s1) == 0:
        s2, s1 = s1, s2
    sequences = []
    for places in choose(range(length), len(s1)):
        sequence = [None]*length
        for i, place in enumerate(places):
            sequence[place] = s1[i]
        for i, place in enumerate(set(range(length)).difference(places)):
            sequence[place] = s2[i]
        sequences.append(sequence)
    return sequences


def BST_Sequences(bst):
    if bst is None:
        return [[]]

    seqs1 = BST_Sequences(bst.lchild)
    seqs2 = BST_Sequences(bst.rchild)
    seqs = []
    for l in seqs1:
        for r in seqs2:
            seqs.extend(mix_seqs(l,r))
    for i in range(len(seqs)):
        seqs[i] = [bst.value] + seqs[i]
    return seqs


then = datetime.now()
tree = BST([x for x in range(14)])
print(len(BST_Sequences(tree)))
print(datetime.now() - then)








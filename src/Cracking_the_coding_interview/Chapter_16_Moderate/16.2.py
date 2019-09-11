# Word Frequencies: Design a method to find the frequency of occurrences of any given word in a book.
# What if we were running this algorithm multiple times?


def frequency(word, document):
    f = 0
    total = 0
    for item in document:
        if item == word:
             f += 1
        total += 1
    return f/total


def word_counter(document):
    counter = dict()
    total = 0
    for item in document:
        if counter.get(item) is None:
            counter[item] = 1
        else:
            counter[item] += 1
        total += 1
    return counter, total


# If we want to count many documents then we can use a map reduce cluster
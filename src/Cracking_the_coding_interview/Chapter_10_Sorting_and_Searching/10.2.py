import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from sorting.insertionsort import insertionsort


def sort_anagrams(arr: list):
    """
    #177, #182, #263, #342
    first insertion sort the words
    then quick sort the array by the letters in the word
    Time:
    Space:
    :param arr:
    :return:
    """
    word_counts = {(word, ''.join(insertionsort(word))) for word in arr}

    return [x[0] for x in sorted(word_counts, key=lambda x: x[1])]


tester = ['bob', 'she', 'obb', 'supercaloous', 'hes', 'arrarat', 'bobby', 'abo']
print(sort_anagrams(tester))

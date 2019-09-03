# Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have
# duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how would you print
# all duplicate elements in the array?

# distributed merge sort, 1000 numbers at a time, or use the file system to do a radix sort in the directory, then
# scan the files
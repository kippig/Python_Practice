from functools import reduce

class Solution:
    def makesquare(self, nums) -> bool:
        # Can split array into 4 groups of equal sum.
        # First, sum the array
        perimeter = sum(nums)
        if perimeter % 4 != 0:
            return False
        edge = perimeter / 4

        nums.sort()
        if nums[-1] > edge:
            return False

        return self.distribute_groups(arr=nums, edge=edge)

    def distribute_groups(self, arr, edge, buckets=None):
        if len(arr) == 0:
            return sum(list(map(lambda x: x['Sum'] == edge, buckets))) == 4

        if buckets is None:
            buckets = [{'Sum': 0}, {'Sum': 0}, {'Sum': 0}, {'Sum': 0}]

        for i in range(len(arr) - 1, -1, -1):
            for bucket in buckets:
                print(buckets)
                if bucket['Sum'] + arr[i] <= edge:
                    if bucket.get(arr[i]) is None:
                        bucket[arr[i]] = 1
                    else:
                        bucket[arr[i]] += 1
                    bucket['Sum'] += arr[i]
                    temp = arr.pop()
                    if self.distribute_groups(arr, edge, buckets):
                        return True
                    else:
                        arr.append(temp)
                        bucket[arr[i]] -= 1
                        bucket['Sum'] -= arr[i]
                        if bucket[arr[i]] <= 0:
                            del bucket[arr[i]]
        return False


bob = Solution()
print(bob.makesquare([99, 37, 37, 37, 37, 37, 37, 37, 37, 5]))

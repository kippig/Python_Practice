from datetime import datetime


class Primes:
    @staticmethod
    def stream(limit=15486258):
        # requires scanning the array twice :/
        array = [True]*(limit+1)

        odd = 3
        while odd <= int(limit**0.5) + 1:
            if array[odd]:
                j = odd**2
                while j <= limit:
                    array[j] = False
                    j = j + odd
            odd += 2

        yield 2
        i = 3
        while i <= limit:
            if array[i]:
                yield i
            i += 2


def verify(from_n, frequency=1000,):
    stream = Primes.stream(limit=from_n + 1)
    for k in range(from_n):
        latest = next(stream)
        if k % frequency == 0:
            print(latest)


t = datetime.now()
verify(100, frequency=1)
print("Process ran in {}".format(datetime.now()-t))

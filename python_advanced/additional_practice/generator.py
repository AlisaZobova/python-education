"""Class-generator for fibonacci numbers"""

#  pylint: disable=C0103


class GeneratorFibonacci:
    """Class-generator for fibonacci numbers"""
    def __init__(self):
        self.num = 0
        self.next_num = 1
        self.max_num = 50

    def new_num(self):
        """Generate new num"""
        if self.max_num:
            self.num, self.next_num = self.next_num, self.num + self.next_num
            self.max_num -= 1
            return self.num
        raise StopIteration

    def __next__(self):
        return self.new_num()

    def __iter__(self):
        return self


fibonacci1 = GeneratorFibonacci()

for i in fibonacci1:
    print(i)

fibonacci2 = GeneratorFibonacci()

for i in range(5):
    print(next(fibonacci2))

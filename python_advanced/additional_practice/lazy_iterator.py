"""Lazy iterators"""
import itertools  # for self-test

#  pylint: disable=C0103


class Zip:
    """Zip"""
    def __init__(self, *iterables):
        self.iterables = iterables
        self.zip_len = min((len(i) for i in iterables))
        self.el_num = 0

    def gen_zip_el(self):
        """Generate new element"""
        if self.zip_len:
            zip_el = tuple([i[self.el_num] for i in self.iterables])
            self.el_num += 1
            self.zip_len -= 1
            return zip_el
        raise StopIteration

    def __next__(self):
        return self.gen_zip_el()

    def __iter__(self):
        return self


print("Zip:\n")

a = [1, 2, 3]
b = "drchuu"
c = (5, 3)

zip1 = Zip(a, b, c)

print("Result:")

for zip_elem in zip1:
    print(zip_elem)


class Chain:
    """Chain"""
    def __init__(self, *iterables):
        self.iterables = iterables
        self.chain_len = sum((len(i) for i in iterables))
        self.el_num = 0
        self.it_num = 0

    def gen_chain_el(self):
        """Generate new element"""
        if self.chain_len:
            if self.el_num == len(self.iterables[self.it_num]):
                self.it_num += 1
                self.el_num = 0
            elem = self.iterables[self.it_num][self.el_num]
            self.el_num += 1
            self.chain_len -= 1
            return elem
        raise StopIteration

    def __next__(self):
        return self.gen_chain_el()

    def __iter__(self):
        return self


print("\nChain:\n")

a = [1, 2, 3]
b = "drchuu"
c = (5, 3)

chain1 = Chain(a, b, c)

print("Result:")

for chain_elem in chain1:
    print(chain_elem, end=" ")


class PairCombinations:
    """Class for pair combinations"""
    def __init__(self, *iterables):
        self.iterables = iterables
        self.elements = [iterables[it_num][el_num] for it_num in range(len(iterables))
                         for el_num in range(len(self.iterables[it_num]))]
        self.combinations_set = list(set(self.elements))
        self.combinations_len = len(self.elements)
        self.el_num = 0
        self.mul_num = 1

    def gen_combinations_el(self):
        """Generate new element"""
        if self.combinations_len:
            if self.mul_num == self.combinations_len:
                self.elements.remove(self.elements[self.el_num])
                self.combinations_len = len(self.elements)
                self.mul_num = 1
            if self.combinations_len > 1:
                elem = (self.elements[self.el_num], self.elements[self.mul_num])
                self.mul_num += 1
                return elem
        raise StopIteration

    def __next__(self):
        return self.gen_combinations_el()

    def __iter__(self):
        return self


a = [1, 2]
b = "druu"
c = (5, 3)

print("\n\nCombinations:\n")

combi1 = PairCombinations(a, b, c)

print("Result:")

print("If use itertools.combinations:")
print(*list(itertools.combinations(combi1.elements, 2)))

print("If use my PairCombinations class:")
for combi_elem in combi1:
    print(combi_elem, end=' ')


class Product:
    """Product"""
    def __init__(self, *iterables):
        self.iterables = list(iterables)

    def gen_product(self):
        """Generate new element"""
        product = lambda x, y: ((i, j) if isinstance(i, int) else (*i, j) for i in x for j in y)
        result = product(self.iterables[0], self.iterables[1])
        for i in self.iterables[2:]:
            result = product(result, i)
        return result

    def __iter__(self):
        return self.gen_product()


a = [1, 2, 3]
b = "druu"
c = (5, 3, 2, 5, 6)
d = (8, 1, 6, 2, 5)

print("\n\nProduct:\n")

product1 = Product(a, b, c, d)

print("Result 1:")

print("If use itertools.product:")
print(*itertools.product(a, b, c, d))

print("If use my Product class:")
for prod_elem in product1:
    print(prod_elem, end=' ')

product2 = Product(a, b)

print("\nResult 2:")

print("If use itertools.product:")
print(*itertools.product(a, b))

print("If use my Product class:")
for prod_elem in product2:
    print(prod_elem, end=' ')

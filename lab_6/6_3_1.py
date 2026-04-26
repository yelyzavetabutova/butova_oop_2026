from lab_5.Rational import Rational
from lab_5.RationalList import RationalList as BaseRationalList

class RationalIterator:
    def __init__(self, elements):
        data_to_sort = list(elements)
        lst = []
        for i in range(len(data_to_sort)):
            r = data_to_sort[i]
            lst.append((r.d, r.n, i, r))
        lst.sort(reverse=True)

        self.sorted_data = []
        for item in lst:
            self.sorted_data.append(item[3])
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_data):
            res = self.sorted_data[self.index]
            self.index += 1
            return res
        raise StopIteration

    def __iter__(self):
        return self

class RationalList(BaseRationalList):
    def __iter__(self):
        return RationalIterator(self.elements)

filenames = ["input01.txt", "input02.txt", "input03.txt"]
for name in filenames:
    r_list = RationalList()
    r_list.elements = []g
        with open(name, 'r') as f:
            for word in f.read().split():
                r_list += Rational(word)

        print(f"\n Результати для файлу: {name}")
        for r in r_list:
            print(f"Число: {r} (n={r.n}, d={r.d})")
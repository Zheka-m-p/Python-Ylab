from itertools import cycle


class CyclicIterator:
    def __init__(self, iter_obj):
        self.iter_obj = cycle(iter_obj)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter_obj)


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)

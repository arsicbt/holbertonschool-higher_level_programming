class CountedIterator():
    def __init__(self, i):
        self.iter = iter(i)
        self.count = 0

    def __next__(self):
        item = next(self.iter)
        try:
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        return self.count

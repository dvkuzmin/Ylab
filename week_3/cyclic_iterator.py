from typing import Iterable
from collections import deque
from time import sleep


class CyclicIterator:
    """Class create iterators, which return values in collection in cycle"""
    def __init__(self, container: Iterable):
        self.counter = 0
        self.queue = deque()
        for element in container:  # fill queue for the first time
            self.queue.append(element)

    def __iter__(self):
        return self

    def __next__(self):
        result = self.queue.popleft()
        self.queue.append(result)
        sleep(0.3)
        return result


if __name__ == "__main__":
    #  Example 1
    cyclic_iterator = CyclicIterator({1: 'first', 2: 'second', 3: 'third'})

    for i in cyclic_iterator:
        print(i)

    # # Example 2
    # cyclic_iterator_2 = CyclicIterator((1, 2, 3))
    #
    # for i in cyclic_iterator_2:
    #     print(i)
    #
    # #Example 3
    # cyclic_iterator_3 = CyclicIterator(range(3))
    #
    # for i in cyclic_iterator_3:
    #     print(i)

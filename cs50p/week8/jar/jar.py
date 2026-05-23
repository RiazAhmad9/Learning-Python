class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if isinstance(n, int) and self.size + n <= self._capacity and n > 0:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if isinstance(n, int) and n <= self.size and n > 0:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
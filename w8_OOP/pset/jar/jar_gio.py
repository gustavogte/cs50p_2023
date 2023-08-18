class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There are less cookies in Jar")
        self._size -= n

    # Getter equivalent
    @property
    def capacity(self):
        return self._capacity
    # You cannot have a method and an atrribute call capacity
    # they conflict with each other. So you have tu add "_" before
    # the attribunte capacity
    # and added whenever we assigned a value

    # Getter
    @property
    def size(self):
        return self._size
    # happens the same problem of capacity

"""
jar = Jar()
jar.deposit(2)
jar.withdraw(1)
print(jar)
"""
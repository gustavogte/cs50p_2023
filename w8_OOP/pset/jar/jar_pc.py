class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0


    def __str__(self):
        return "🍪" * self.size



    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n


    # Getter
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

def main():
    jar = Jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()

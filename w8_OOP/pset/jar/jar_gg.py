class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        n = int(self.size)
        c = n * "🍪"
        # siempre se tiene que regresar un string
        return f"{c}"


    def deposit(self, n):
        n = int(input("Cookie deposit: "))
        self.size = self.size + n
        if self.size <= self.capacity:
            return Jar()
        else:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        n = int(input("Cookie withdraw: "))
        if self.size >= n:
            self.size = self.size - n
        else:
            raise ValueError("Not enough cookies")
        return Jar()

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # ==> nuevo Setter
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != type(int()) or int(capacity) < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    # Getter
    @property
    def size(self):
        return self._size

# ==> nuevo Setter
    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    print("capacity: ", jar.capacity)
    print("size: ", jar.size)
    print(jar)

    jar.deposit(1)
    print(jar)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()

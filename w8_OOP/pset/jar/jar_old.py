class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        n = int(self.capacity)
        c = n * "🍪"
        # siempre se tiene que regresar un string
        return f"{c}"


    def deposit(self, n):
        n = int(input("Cookie deposit:"))
        self.capacity = self.capacity + n
        if self.capacity <= 12:
            return Jar()
        else:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        n = int(input("Cookie withdraw:"))
        self.capacity = self.capacity - n
        if self.capacity > 0:
            return Jar()
        else:
            raise ValueError("Not enough cookies")

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

    @property
    def size(self):
        return self.capacity

gus_jar = Jar(5)
print(gus_jar)
gus_jar.deposit(2)
print(gus_jar)
gus_jar.withdraw(2)
print(gus_jar)
print(gus_jar.size)
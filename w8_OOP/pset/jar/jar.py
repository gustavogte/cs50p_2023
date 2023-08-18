class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # siempre se tiene que regresar un string
        return self.size * "🍪"


    def deposit(self, n):
        #n = int(input("Cookie deposit: "))
        # primero poner las condiciones
        if n > self.capacity:
            raise ValueError("Too many cookies")
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies 2")
        self._size += n

    def withdraw(self, n):
        #n = int(input("Cookie withdraw: "))
        if self.size < n:
            raise ValueError("Not enough cookies")
        self._size -= n

    # Getter property equivalente getters or setters
    @property
    def capacity(self):
        return self._capacity
    # You cannot have a method and an atrribute call capacity
    # they conflict with each other. So you have tu add "_" before
    # the attribunte capacity
    # and added whenever we assigned a value

    ## Los setters están el en init incluidos

    # Getter
    @property
    def size(self):
        return self._size

    # los setters están el en init
"""
def main():
    jar = Jar()
    print(jar.capacity)
    print(jar)
    jar.deposit(2)
    print(jar)
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    print(jar)

if __name__ == "__main__":
    main()
"""
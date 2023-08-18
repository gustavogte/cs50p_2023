from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    gus_jar = Jar()
    assert str(gus_jar) == ""
    gus_jar.deposit(1)
    assert print(str(gus_jar.size)) == "🍪"
    gus_jar.deposit(11)
    assert print(gus_jar.size) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(14) == ValueError("Invalid capacity")


def test_withdraw():
    jar = Jar()
    jar.withdraw(1) == ValueError("Not enough cookies")

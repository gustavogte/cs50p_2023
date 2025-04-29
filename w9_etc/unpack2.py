"""
def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


f(100, 50, 25)
f(galleons=50, sickless=50, knuts=25)


def print(*objects, sep=" ", end="\n", ):
    for object in objects:
        ...
"""
def g(*gus, **kgus):
    print("Posición:", gus)
    print("Nombrados:", kgus)

g(20, 40, 122)
g(nombre="gus", apellido="gtz", edad=50)

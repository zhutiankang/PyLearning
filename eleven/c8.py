
def factory():
    origin = 0
    def go(step):
        nonlocal origin
        origin = origin + step
        return origin
    return go

f = factory()
print(f(2))
print(f(6))
print(f(8))
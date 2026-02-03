x=10

def show():
    x=5
    print(x)

show()
print(x)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

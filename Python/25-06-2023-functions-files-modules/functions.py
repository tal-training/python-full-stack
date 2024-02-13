def a():
    print("start a()")
    b()
    c()
    print("fin a()")

def b():
    print("start b()")
    d()
    print("fin b()")

def c():
    print("start c()")
    d()
    print("fin c()")

def d():
    print("start and fin d()")

a()
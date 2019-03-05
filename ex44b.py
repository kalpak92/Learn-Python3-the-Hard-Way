#Method Order Resolution

O = object


class F(O):
    pass


class E(O):
    pass


class D(F, E):
    pass


class C(E, F):
    pass

class B(C, D):
    pass

print("Success")



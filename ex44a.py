#Method Order Resolution

O = object


class F(O):
    pass


class E(O):
    pass


class D(O):
    pass


class C(D,F):
    pass


class B(D,E):
    pass


class A(B,C):
    pass

print(F.__mro__)
print(E.__mro__)
print(D.__mro__)
print(C.__mro__)
print(B.__mro__)
print (A.__mro__)

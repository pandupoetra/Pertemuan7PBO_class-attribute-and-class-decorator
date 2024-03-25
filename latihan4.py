def pembagian(func):
    def inner(a, b):
        print(f"pembagian {a} dengan {b}")
        if b == 0:
            print("tidak bisa melakukan pembagian dengan 0")
            return
        return func(a, b)
    return inner

@pembagian
def bagi(a, b):
    print("hasil pembagiannya adalah",a/b)

bagi(2,5)
print()
bagi(2,0)
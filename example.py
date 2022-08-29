from filterablelist.filterablelist import FilterableList

class MyClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self) -> str:
        return f"(x:{self.x}, y:{self.y}, z:{self.z})"


fl = FilterableList([
    MyClass(1, 1, 1),
    MyClass(1, 1, 2),
    MyClass(2, 1, 3),
    {"x": 1, "y": 2, "z": 1}
])

print()
print("="*100)
print("|"*100)
print("="*100)
print(fl.filter(x=1))
print(fl.filter(x=1, y=1))
print(fl.filter(x=1, y=1, require_all=False))
print(fl.filter(y__in=[2,5,7]))

print(fl.exclude(x=1))
print(fl.exclude(x=1, y=1))
print(fl.exclude(x=1, y=1, require_all=False))
print(fl.exclude(y__in=[2,5,7]))

print()
print("="*100)
print(fl.filter(z__lte=2))
print(fl.exclude(x__lt=2))
print(fl.filter(x__ne=1))

print()
print("="*100)
fl = FilterableList([
    {"a": 1, "b": False, "c": None},
    {"a": 2, "b": False, "c": None},
    {"a": 1, "b": False, "c": 5},
    {"a": 1, "b": False, "c": True},
    {"a": 1, "d": []}
])

new_fl = fl.filter(a=1).exclude(c__bte=4).filter(c__ne=True)

print(new_fl)
print()
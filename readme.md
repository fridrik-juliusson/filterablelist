# filterable-list

A subclass of Python's built in `list`, with two additional methods inspired by the `filter` and `exclude` methods from the Django queryset.

## Use example

```python
from filterablelist import FilterableList

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
    {"x": 1, "y": 1, "z": 1}
])


print(fl.filter(x=1))
print(fl.filter(x=1, y=2))
print(fl.filter(x=1, z=2))

print(fl.exclude(x=1))
print(fl.exclude(x=1, y=2))
print(fl.exclude(x=1, z=2))

# Output
# [(x:1, y:1, z:1), (x:1, y:1, z:2), {'x': 1, 'y': 1, 'z': 1}]
# []
# [(x:1, y:1, z:2)]
# [(x:2, y:1, z:3)]
# [(x:2, y:1, z:3)]
# [(x:2, y:1, z:3)]

```

## filter(`check_subscriptable=True`, `require_all=True`, `**kwargs`)

### Arguments

`check_subscriptable`: Boolean, True by default.

The `filter` method takes any number of key-value pairs as arguments, and will then filter a list of almost any type of objects based on the query

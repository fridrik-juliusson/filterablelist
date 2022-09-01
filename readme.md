# filterablelist

A subclass of Python's built in `list`, with two additional methods inspired by the `filter` and `exclude` methods from the Django queryset. These methods allows for complex list filtering with a very simple syntax.

## Use examples

**Create an example list:**

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
    {"x": 1, "y": 2, "z": 1}
])
```

**Make new lists with simple queries:**

```python
print(fl.filter(x=1))
print(fl.filter(x=1, y=1))
print(fl.filter(x=1, y=1, require_all=False))
print(fl.filter(y__in=[2,5,7]))

print(fl.exclude(x=1))
print(fl.exclude(x=1, y=1))
print(fl.exclude(x=1, y=1, require_all=False))
print(fl.exclude(y__in=[2,5,7]))

# Output
>>> [(x:1, y:1, z:1), (x:1, y:1, z:2), {'x': 1, 'y': 2, 'z': 1}]
>>> [(x:1, y:1, z:1), (x:1, y:1, z:2)]
>>> [(x:1, y:1, z:1), (x:1, y:1, z:2), (x:2, y:1, z:3), {'x': 1, 'y': 2, 'z': 1}]
>>> [{'x': 1, 'y': 2, 'z': 1}]

>>> [(x:2, y:1, z:3)]
>>> [(x:2, y:1, z:3), {'x': 1, 'y': 2, 'z': 1}]
>>> []
>>> [(x:1, y:1, z:1), (x:1, y:1, z:2), (x:2, y:1, z:3)]
```

**Use comparison operator postfixes to make more complex queries:**

```python
print(fl.filter(z__lte=2))
print(fl.exclude(x__lt=2))
print(fl.filter(x__ne=1))

# Output
>>> [(x:1, y:1, z:1), (x:1, y:1, z:2), {'x': 1, 'y': 2, 'z': 1}]
>>> [(x:2, y:1, z:3)]
>>> [(x:2, y:1, z:3)]
```

## Methods

_Note: All methods and properties of the built-in `list` are also available._

### filter(`check_subscriptable=True`, `require_all=True`, `**kwargs`)

**Arguments**

`check_subscriptable`: Boolean, True by default. If True, the filter will match against subscriptable indexes where available, as well as object properties. Set to False to only match against object properties.

`require_all`: Boolean, True by Default. When True, only objects that match all arguments will be included in the new list (similar to using `AND` in an SQL query.) When set to False, all objects that match any of the arguments will be included in the new list (similar to using `OR` in an SQL query.)

`**kwargs`: Any number of key-value pairs that you wish to filter the list by.

**Description**

The `filter` method takes any number of key-value pairs as arguments and returns a new FilterableList containing only the matching objects. By default, all arguments have to match for an object to be included, and both object properties and subscriptable indexes will be used to try to match objects. This default behaviour can be changed by setting `require_all` and/or `check_subscriptable` to `False` per your requirements.

### exclude(`check_subscriptable=True`, `require_all=True`, `**kwargs`)

**Arguments**

`check_subscriptable`: Boolean, True by default. If True, exclude will match against subscriptable indexes where available, as well as object properties. Set to False to only match against object properties.

`require_all`: Boolean, True by Default. When True, only objects that match all arguments will be excluded in the new list (similar to using `AND` in an SQL query.) When set to False, all objects that match any of the arguments will be excluded in the new list (similar to using `OR` in an SQL query.)

`**kwargs`: Any number of key-value pairs that you want to use to exclude objects from the new list.

**Description**

Basically the same as `filter` except that items that match the query will be excluded from the new list, rather than included.

## Comparison Operators

By default, both `filter` and `exclude` will match object properties to arguments using the equality operator ´==´, but by adding a comparison postfix to the keys in your query, you can create more complex filters. The comparison operators available are:

-   **\_\_gt** : _(Greater than)_ Uses Python's `>` operator for comparison.
-   **\_\_gte** : _(Greater than or equal to)_ Uses Python's `>=` operator for comparison.
-   **\_\_lt** : _(Less than)_ Uses Python's `<` operator for comparison.
-   **\_\_lte** : _(Less than or equal to)_ Uses Python's `<=` operator for comparison.
-   **\_\_ne** : _(Not equal to)_ Uses Python's `!=` operator for comparison.
-   **\_\_in** : _(Not equal to)_ Uses Python's `in` operator for comparison.

**Examples**

```python
# name is equal to "Isaac" (default comparison without postfix)
.filter(name="Isaac")

# count is greater than 5
.filter(count__gt=5)

# age is greater than or equal to 111
.filter(age__gte=111)

# clicks is less than 19
.filter(clicks__lt=19)

# score is less than or equal to 1200
.filter(score__lte=1200)

# state is not equal to None
.filter(state__ne=None)

# id is in [12, 13, 14]
.filter(id__in=[12, 13, 14])
```

## Query Chaining

Both `filter` and `exclude` returns a new FilterableList, making it possible to chain queries together if needed.

```python
from filterablelist import FilterableList

fl = FilterableList([
    {"a": 1, "b": False, "c": None},
    {"a": 2, "b": False, "c": None},
    {"a": 1, "b": False, "c": 5},
    {"a": 1, "b": False, "c": True},
    {"a": 1, "d": []}
])

new_fl = fl.filter(a=1).exclude(c__bte=4).filter(c__ne=True)

print(new_fl)

# Output
# [{'a': 1, 'b': False, 'c': None}, {'a': 1, 'b': False, 'c': 5}]
```

## Performance

Most normal list operations have no performance drop at all compared to a regular list. Only the operations that return a new list, such as `slice` and `copy` will have any drop in performance, but even in those cases it's very negligible (on the scale of 20%-ish.)

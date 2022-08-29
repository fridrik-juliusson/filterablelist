class FilterableList(list):
    @staticmethod
    def _meets_requirements(item, key, value, check_subscriptable):
        try:
            if hasattr(item, "__getitem__") and check_subscriptable:
                return (
                    item[key[:-5]] >= value if key[-5:] == "__gte" else
                    item[key[:-5]] <= value if key[-5:] == "__lte" else
                    item[key[:-4]] > value if key[-4:] == "__gt" else
                    item[key[:-4]] < value if key[-4:] == "__lt" else
                    item[key[:-4]] != value if key[-4:] == "__ne" else
                    item[key[:-4]] in value if key[-4:] == "__in" else
                    item[key] == value
                )
            else:
                return (
                    getattr(item, key[:-5], None) >= value if key[-5:] == "__gte" else
                    getattr(item, key[:-5], None) <= value if key[-5:] == "__lte" else
                    getattr(item, key[:-4], None) > value if key[-4:] == "__gt" else
                    getattr(item, key[:-4], None) < value if key[-4:] == "__lt" else
                    getattr(item, key[:-4], None) != value if key[-4:] == "__ne" else
                    getattr(item, key[:-4], None) in value if key[-4:] == "__in" else
                    getattr(item, key, None) == value
                )
        except (TypeError, KeyError, IndexError):
            return False

    def filter(self, *args, check_subscriptable=True, require_all=True, **kwargs):
        return self.__class__(
            item for item in self if (
                all(self._meets_requirements(item=item, key=key, value=value, check_subscriptable=check_subscriptable) for (key, value) in kwargs.items()) if require_all else 
                any(self._meets_requirements(item=item, key=key, value=value, check_subscriptable=check_subscriptable) for (key, value) in kwargs.items())
            )
        )

    def exclude(self, *args, check_subscriptable=True, require_all=True, **kwargs):
        return self.__class__(
            item for item in self if (
                not all(self._meets_requirements(item=item, key=key, value=value, check_subscriptable=check_subscriptable) for (key, value) in kwargs.items()) if require_all else 
                not any(self._meets_requirements(item=item, key=key, value=value, check_subscriptable=check_subscriptable) for (key, value) in kwargs.items())
            )
        )

    def __add__(self, *args, **kwargs):
        return self.__class__(super(self.__class__, self).__add__(*args, **kwargs))
    
    def __sub__(self, *args, **kwargs):
        return self.__class__(super(self.__class__, self).__sub__(*args, **kwargs))
    
    def __mul__(self, *args, **kwargs):
        return self.__class__(super(self.__class__, self).__mul__(*args, **kwargs))

    def copy(self):
        return self.__class__(super().copy())

    def __getitem__(self, *args, **kwargs):
        return self.__class__(super().__getitem__(*args, **kwargs))
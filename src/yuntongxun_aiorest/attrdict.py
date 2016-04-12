__all__ = ['recursive_attrdict', 'AttrDict']


def recursive_attrdict(obj):
    """
    Walks a simple data structure, converting dictionary to AttrDict.
    Supports lists, tuples, and dictionaries.
    """
    if isinstance(obj, dict):
        return AttrDict(dict((str(k), recursive_attrdict(v)) for (k, v) in obj.items()))
    elif isinstance(obj, list):
        return list(recursive_attrdict(i) for i in obj)
    elif isinstance(obj, tuple):
        return tuple(recursive_attrdict(i) for i in obj)
    else:
        return obj


class AttrDict(dict):
    """
    A dictionary with attribute-style access. It maps attribute access to
    the real dictionary.
    """

    def __init__(self, iterable=None, **kwargs):
        super().__init__(iterable or {}, **kwargs)

    def __getstate__(self):
        return self.__dict__.items()

    def __setstate__(self, items):
        for key, val in items:
            self.__dict__[key] = val

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__qualname__, dict.__repr__(self))

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def __getitem__(self, name):
        return super().__getitem__(name)

    def __delitem__(self, name):
        return super().__delitem__(name)

    __getattr__ = __getitem__
    __setattr__ = __setitem__

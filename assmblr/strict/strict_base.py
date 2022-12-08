from collections import OrderedDict


class _StrictlyMeta(type):
    def __or__(cls, other):
        return cls(other)

    def __ror__(cls, other):
        return cls(other)


class Strictly(metaclass = _StrictlyMeta):
    __slots__ = ("predicates", "msg", '__name__')
    predicate_cache = OrderedDict()

    def __init__(
            self,
            *predicates,
            msg = "Value does not match any of the predicates",
    ):
        self.predicates = predicates
        self.msg = msg

    def __set_name__(self, owner, name):
        self.__name__ = name

    def __set__(self, instance, value):
        if not self.map(value):
            msg = f"attempted to set {self.__name__!r} to {value!r} but {self.msg}"
            raise ValueError(msg)
        instance.__dict__[self.__name__] = value

    def bind(self, *funcs):
        self.predicates += funcs
        return self

    def map(self, value):
        key = id(value)

        if key in self.predicate_cache:
            return self.predicate_cache.setdefault(key, self.predicate_cache.pop(key))

        for predicate in self.predicates:
            if not predicate(value):
                return self.predicate_cache.setdefault(key, False)

        self.predicate_cache.update({key: True})
        return True

    def message(self, msg):
        self.msg = msg
        return self

    def __or__(self, other):
        if isinstance(other, str):
            return self.message(other)
        return self.bind(other)

    def __ror__(self, other):
        return self.__or__(other)


class StrictPredicate(metaclass = _StrictlyMeta):
    __slots__ = ("func",)

    def __init__(self, func):
        self.func = func

    def __call__(self, value):
        return self.func(value)

    def __or__(self, other):
        if callable(other):
            return StrictPredicate(lambda x: self(x) and other(x))
        raise TypeError(f"Cannot combine {self} with {other}")


__all__ = ["Strictly", "StrictPredicate"]

from assmblr.meta import _DescriptorPipelineMeta


class Strictly(metaclass = _DescriptorPipelineMeta):
    __slots__ = ("predicates", "msg", '__name__')
    predicate_cache = {}

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
        is_match = self.map(value)
        if not is_match:
            msg = f"attempted to set {self.__name__!r} to {value!r} but {self.msg}"
            raise ValueError(msg)
        instance.__dict__[self.__name__] = value

    def bind(self, *funcs):
        self.predicates += funcs
        return self

    def map(self, value):
        try:
            key = hash(value)
        except TypeError:
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


class StrictPredicate(metaclass = _DescriptorPipelineMeta):
    __slots__ = ("func",)

    def __init__(self, func):
        self.func = func

    def __call__(self, value):
        func = self.func
        return func(value)

    def __or__(self, other):
        if callable(other):
            return StrictPredicate(self.combine(self.func, other))
        raise TypeError(f"Cannot combine {self} with {other}")

    @staticmethod
    def combine(func1, func2):
        def combined(x):
            return func1(x) and func2(x)
        return combined


__all__ = ["Strictly", "StrictPredicate"]

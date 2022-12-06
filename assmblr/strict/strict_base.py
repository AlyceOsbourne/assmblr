from collections import OrderedDict


class _StrictlyMeta(type):
    def __or__(cls, other):
        return cls(other)

    def __ror__(cls, other):
        return cls(other)


class StrictlyDescriptor(metaclass = _StrictlyMeta):
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
            raise ValueError(self.msg)
        instance.__dict__[self.__name__] = value

    def bind(self, *funcs):
        self.predicates += funcs
        return self

    def map(self, value):
        try:
            key = hash(value)
        except TypeError:
            """If the value is unhashable, we can't cache it"""
        else:
            if key in self.predicate_cache:
                return self.predicate_cache[key]
        result = True
        for predicate in self.predicates:
            if not predicate(value):
                result = False
                break
        try:
            return self.predicate_cache.setdefault(key, result)  # NOQA
        except NameError:
            return result

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
    def __init__(self, *predicates):
        self.predicates = predicates

    def __call__(self, value):
        for predicate in self.predicates:
            if not predicate(value):
                return False
        return True

    def __bind__(self, *funcs):
        self.predicates += funcs
        return self

    def __or__(self, other):
        return self.__bind__(other)

    def __ror__(self, other):
        return self.__bind__(other)




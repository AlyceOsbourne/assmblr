from meta import _DescriptorPipelineMeta


class _Dummy(metaclass = _DescriptorPipelineMeta):
    def __init__(self, value):
        self.value = value

    def __set__(self, instance, value):
        pass


class DummyValue(_Dummy):
    def __or__(self, other):
        self.value = other
        return self

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value


class DummyFunction(_Dummy):
    def __call__(self, *args, **kwargs):
        return self

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return lambda *args, **kwargs: self.value(instance, *args, **kwargs)


if __name__ == "__main__":
    class Test:
        a = DummyValue | 1

        @DummyFunction(lambda self, x: 10)
        def b(self, x):
            return x

        def __init__(self):
            self.a = 2


    t = Test()
    print(t.a)
    print(t.b(1))
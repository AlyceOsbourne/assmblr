from meta import _DescriptorPipelineMeta


class _Dummy(metaclass = _DescriptorPipelineMeta):
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        pass


class DummyValue:
    def __or__(self, other):
        self.value = other
        return self


class DummyFunction(_Dummy):
    def __call__(self, *args, **kwargs):
        return self.value




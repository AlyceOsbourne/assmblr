class _DescriptorPipelineMeta(type):
    def __or__(cls, other):
        return cls(other)

    __ror__ = __or__

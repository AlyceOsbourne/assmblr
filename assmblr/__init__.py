from strict import *

if __name__ == "__main__":
    from dataclasses import dataclass
    is_pos_int = StrictPredicate | (lambda x: isinstance(x, int)) | (lambda x: x > 0)
    @dataclass
    class Foo:
        x: int = StrictlyDescriptor | is_pos_int | "must be a positive integer"

    foo = Foo(10)
    print(foo.x)

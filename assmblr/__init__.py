from strict import Strictly, is_positive_int, is_positive_number, is_positive_float


if __name__ == "__main__":
    class Foo:
        x = Strictly | is_positive_int | "x must be a positive integer"
        y = Strictly | is_positive_float | "y must be a positive float"
        z = Strictly | is_positive_number | "z must be a positive number"

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    class Bar:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        @staticmethod
        def is_pos_int(val):
            return isinstance(val, int) and val > 0

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, value):
            if not self.is_pos_int(value):
                raise ValueError("x must be a positive integer")
            self._x = value

        @property
        def y(self):
            return self._y

        @y.setter
        def y(self, value):
            if not isinstance(value, float) or value <= 0:
                raise ValueError("y must be a positive float")
            self._y = value

        @property
        def z(self):
            return self._z

        @z.setter
        def z(self, value):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("z must be a positive number")
            self._z = value
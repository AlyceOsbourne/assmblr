from collections import abc

from .strict_base import Strictly, StrictPredicate

# numbers
is_int = StrictPredicate(lambda x: isinstance(x, int))
is_float = StrictPredicate(lambda x: isinstance(x, float))
is_number = StrictPredicate(lambda x: isinstance(x, (int, float)))

is_zero = StrictPredicate(lambda x: x == 0)
is_non_zero = StrictPredicate(lambda x: x != 0)
is_positive = StrictPredicate(lambda x: x > 0)
is_negative = StrictPredicate(lambda x: x < 0)
is_non_negative = StrictPredicate(lambda x: x >= 0)
is_non_positive = StrictPredicate(lambda x: x <= 0)
is_positive_int = is_int | is_positive
is_negative_int = is_int | is_negative
is_non_negative_int = is_int | is_non_negative
is_non_positive_int = is_int | is_non_positive
is_positive_float = is_float | is_positive
is_negative_float = is_float | is_negative
is_non_negative_float = is_float | is_non_negative
is_non_positive_float = is_float | is_non_positive
is_positive_number = is_number | is_positive
is_negative_number = is_number | is_negative
is_non_negative_number = is_number | is_non_negative
is_non_positive_number = is_number | is_non_positive

is_complex = StrictPredicate(lambda x: isinstance(x, complex))
is_real = StrictPredicate(lambda x: isinstance(x, (int, float, complex)))

# sized predicates
is_empty = StrictPredicate(lambda x: len(x) == 0)
is_non_empty = StrictPredicate(lambda x: len(x) != 0)

# strings
is_string = StrictPredicate(lambda x: isinstance(x, str))
is_empty_string = is_string | is_empty
is_non_empty_string = is_string | is_non_empty
is_string_of_length = lambda n: is_string | (lambda x: len(x) == n)
is_string_of_length_at_least = lambda n: is_string | (lambda x: len(x) >= n)
is_string_of_length_at_most = lambda n: is_string | (lambda x: len(x) <= n)
is_string_of_length_between = lambda a, b: is_string | (lambda x: a <= len(x) <= b)
is_ascii_string = is_string | str.isascii
is_unicode_string = is_string | (lambda x: not str.isascii(x))

lowercase = StrictPredicate(str.islower)
uppercase = StrictPredicate(str.isupper)
titlecase = StrictPredicate(str.istitle)
capitalized = StrictPredicate(str.istitle)
is_alpha = StrictPredicate(str.isalpha)
is_alphanumeric = StrictPredicate(str.isalnum)
is_numeric = StrictPredicate(str.isnumeric)
is_decimal = StrictPredicate(str.isdecimal)
is_digit = StrictPredicate(str.isdigit)
is_identifier = StrictPredicate(str.isidentifier)
is_title = StrictPredicate(str.istitle)

# sequences
is_tuple = StrictPredicate(lambda x: isinstance(x, tuple))
is_list = StrictPredicate(lambda x: isinstance(x, list))
is_set = StrictPredicate(lambda x: isinstance(x, set))
is_frozenset = StrictPredicate(lambda x: isinstance(x, frozenset))
is_dict = StrictPredicate(lambda x: isinstance(x, dict))
is_mapping = StrictPredicate(lambda x: isinstance(x, abc.Mapping))
is_sequence = StrictPredicate(lambda x: isinstance(x, abc.Sequence))
is_iterable = StrictPredicate(lambda x: isinstance(x, abc.Iterable))
is_iterator = StrictPredicate(lambda x: isinstance(x, abc.Iterator))
is_reversible = StrictPredicate(lambda x: isinstance(x, abc.Reversible))
is_container = StrictPredicate(lambda x: isinstance(x, abc.Container))
is_sized = StrictPredicate(lambda x: isinstance(x, abc.Sized))
is_hashable = StrictPredicate(lambda x: isinstance(x, abc.Hashable))
is_callable = StrictPredicate(lambda x: isinstance(x, abc.Callable))
is_generator = StrictPredicate(lambda x: isinstance(x, abc.Generator))
is_coroutine = StrictPredicate(lambda x: isinstance(x, abc.Coroutine))
is_async_generator = StrictPredicate(lambda x: isinstance(x, abc.AsyncGenerator))
is_async_iterator = StrictPredicate(lambda x: isinstance(x, abc.AsyncIterator))

__all__ = ["Strictly", "StrictPredicate"]

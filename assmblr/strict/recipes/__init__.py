from ..strict_base import StrictPredicate

IsNotNone = StrictPredicate | (lambda x: x is not None)
IsNone = StrictPredicate | (lambda x: x is None)
IsTrue = StrictPredicate | (lambda x: x is True)
IsFalse = StrictPredicate | (lambda x: x is False)
IsBool = StrictPredicate | (lambda x: isinstance(x, bool))
IsInt = StrictPredicate | (lambda x: isinstance(x, int))
IsFloat = StrictPredicate | (lambda x: isinstance(x, float))
IsNumber = StrictPredicate | (lambda x: isinstance(x, (int, float)))
IsStr = StrictPredicate | (lambda x: isinstance(x, str))
IsBytes = StrictPredicate | (lambda x: isinstance(x, bytes))
IsByteStr = StrictPredicate | (lambda x: isinstance(x, (str, bytes)))
IsList = StrictPredicate | (lambda x: isinstance(x, list))
IsTuple = StrictPredicate | (lambda x: isinstance(x, tuple))
isDict = StrictPredicate | (lambda x: isinstance(x, dict))
IsSet = StrictPredicate | (lambda x: isinstance(x, set))
IsFrozenSet = StrictPredicate | (lambda x: isinstance(x, frozenset))

IsZero = StrictPredicate | (lambda x: x == 0)
IsNonZero = StrictPredicate | (lambda x: x != 0)

IsPositive = StrictPredicate | (lambda x: x > 0)
IsNegative = StrictPredicate | (lambda x: x < 0)
IsNonNegative = StrictPredicate | (lambda x: x >= 0)
IsNonPositive = StrictPredicate | (lambda x: x <= 0)

IsPositiveInt = IsInt | IsPositive
IsNegativeInt = IsInt | IsNegative
IsNonNegativeInt = IsInt | IsNonNegative
IsNonPositiveInt = IsInt | IsNonPositive

IsPositiveFloat = IsFloat | IsPositive
IsNegativeFloat = IsFloat | IsNegative
IsNonNegativeFloat = IsFloat | IsNonNegative
IsNonPositiveFloat = IsFloat | IsNonPositive

IsPositiveNumber = IsNumber | IsPositive
IsNegativeNumber = IsNumber | IsNegative
IsNonNegativeNumber = IsNumber | IsNonNegative
IsNonPositiveNumber = IsNumber | IsNonPositive

IsAlphabeticStr = IsStr | (lambda x: x.isalpha())
IsAlphanumericStr = IsStr | (lambda x: x.isalnum())
IsDigitStr = IsStr | (lambda x: x.isdigit())
IsLowercaseStr = IsStr | (lambda x: x.islower())
IsUppercaseStr = IsStr | (lambda x: x.isupper())
IsTitlecaseStr = IsStr | (lambda x: x.istitle())
IsSpaceStr = IsStr | (lambda x: x.isspace())
IsPrintableStr = IsStr | (lambda x: x.isprintable())
IsDecimalStr = IsStr | (lambda x: x.isdecimal())
IsNumericStr = IsStr | (lambda x: x.isnumeric())
IsIdentifierStr = IsStr | (lambda x: x.isidentifier())


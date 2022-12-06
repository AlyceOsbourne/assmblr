from strict import *

email_predicate = StrictPredicate | (lambda x: isinstance(x, str)) | (
    lambda x: "@" in x) | "Must be a valid email address"


class Customer:
    email = StrictlyDescriptor(email_predicate) | "Must be a valid email address"

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return f"Customer({self.email!r})"


c = Customer("bob@gmail.com")
print(c)

from enforced_annotations import Strictly
from functools import partial
import datetime

StrictlyDate = partial(Strictly, lambda x: isinstance(x, datetime.date))
StrictlyTime = partial(Strictly, lambda x: isinstance(x, datetime.time))

StrictlyFutureDate = partial(Strictly, lambda x: x > datetime.date.today())
StrictlyFutureTime = partial(Strictly, lambda x: x > datetime.datetime.now().time())

StrictlyPastDate = partial(Strictly, lambda x: x < datetime.date.today())
StrictlyPastTime = partial(Strictly, lambda x: x < datetime.datetime.now().time())
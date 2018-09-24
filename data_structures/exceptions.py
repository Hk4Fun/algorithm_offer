__author__ = 'Hk4Fun'
__date__ = '2018/9/24 17:36'


class BaseError(Exception):
    def __init__(self, info):
        self.info = info

    def __repr__(self):
        return self.info

class EmptyError(BaseError):
    pass

class FullError(BaseError):
    pass

class BaseError(Exception):

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def message(self):
        return self.args[0] if self.args else None

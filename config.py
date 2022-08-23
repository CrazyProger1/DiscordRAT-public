from serializable import SerializableObject


class Config(SerializableObject):
    __filepath__ = 'config.cnf'

    def __init__(self):
        super(Config, self).__init__()

        self.token: str | None = None

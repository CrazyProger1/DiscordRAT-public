from serializable import SerializableObject


class Config(SerializableObject):
    def __init__(self):
        super(Config, self).__init__(self)

        self.token = None

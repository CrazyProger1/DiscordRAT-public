from serializable import SerializableObject

TOKEN = 'MTAxMTYxNzE5MjQ1MTc3MjQ0Ng.GdE7Y8.Mc45D27nfSXXXIKUKe-gxxhVKsl-QkQ6vpo1lE'

class Config(SerializableObject):
    __filepath__ = 'config.cnf'

    def __init__(self):
        super(Config, self).__init__()
        self.token = TOKEN


import os.path
import pickle
from exceptions import *


class SerializableObject:
    """
    Inherited class that implements the saving and loading of the inheritor from a file
    """

    __filepath__: str = 'someobject.s'

    def dump(self):
        """
        Dumps a heritable class instance to a file

        :return:
        """
        with open(self.__filepath__, 'wb') as sf:
            pickle.dump(self, sf)

    @staticmethod
    def load(obj_type):
        """
        Loads a saved class instance from a file

        :param type[SerializableObject] obj_type:
        :return obj_type:
        """
        if not issubclass(obj_type, SerializableObject):
            raise ValueError(f'the obj_type param must be a subclass of {SerializableObject}')

        if os.path.exists(obj_type.__filepath__):
            with open(obj_type.__filepath__, 'rb') as sf:
                instance = pickle.load(sf)
                if isinstance(instance, obj_type):
                    return instance
                else:
                    raise TypeDiscrepancyError(f'loaded instance have wrong type, not {obj_type}')
        else:
            instance = obj_type()
            instance.dump()
            return instance

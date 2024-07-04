from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass

import abc


class Divice(metaclass=abc.ABCMeta):

    @abc.abstractmethod 
    def is_enabled(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def enabled(self):
        raise NotImplementedError

    @abc.abstractmethod
    def disable(self):  
        raise NotImplementedError

    @abc.abstractmethod
    def get_volume(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_volume(self, percent):
        raise NotImplementedError

    @abc.abstractmethod
    def get_channel(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_channel(self, channel):
        raise NotImplementedError

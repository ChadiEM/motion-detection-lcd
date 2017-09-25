import abc


class Trigger(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def turn_on(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def turn_off(self):
        raise NotImplementedError()

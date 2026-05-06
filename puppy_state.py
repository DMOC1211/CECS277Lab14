'''
Name: Jacob Miranda & Daniel Puerto
Date: 5/6/26
Group: 11
Description:
'''

from abc import ABC, abstractmethod

class PuppyState(ABC):
    @abstractmethod
    def feed(self, puppy):
        pass

    @abstractmethod
    def play(self, puppy):
        pass

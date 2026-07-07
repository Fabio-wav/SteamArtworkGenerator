from abc import ABC, abstractmethod

from steam_artwork_generator.models.gif import Gif


class Layer(ABC):

    @abstractmethod
    def apply(self, gif: Gif) -> None:
        pass
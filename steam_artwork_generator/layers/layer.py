from abc import ABC, abstractmethod

from steam_artwork_generator.models import RenderContext


class Layer(ABC):

    @abstractmethod
    def draw(self, context: RenderContext) -> None:
        pass
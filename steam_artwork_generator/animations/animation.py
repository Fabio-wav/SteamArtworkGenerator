from abc import ABC, abstractmethod

from steam_artwork_generator.models import RenderContext


class Animation(ABC):

    @abstractmethod
    def update(self, layer, context: RenderContext) -> None:
        pass
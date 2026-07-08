from abc import ABC, abstractmethod

from steam_artwork_generator.models import (
    Transform,
    RenderContext,
)


class Layer(ABC):

    def __init__(
        self,
        transform: Transform,
        z_index: int = 0,
        visible_from: int = 0,
        visible_until: int | None = None,
    ):
        self.transform = transform
        self.z_index = z_index
        self.visible_from = visible_from
        self.visible_until = visible_until

    @abstractmethod
    def draw(self, context: RenderContext):
        pass

    def is_visible(self, context: RenderContext) -> bool:

        if context.frame_index < self.visible_from:
            return False

        if (
            self.visible_until is not None
            and context.frame_index > self.visible_until
        ):
            return False

        return True
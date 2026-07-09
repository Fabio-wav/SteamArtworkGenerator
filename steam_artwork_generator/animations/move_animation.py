from steam_artwork_generator.animations import Animation
from steam_artwork_generator.models import RenderContext
from steam_artwork_generator.easing import linear


class MoveAnimation(Animation):

    def __init__(
        self,
        start_position: tuple[int, int],
        end_position: tuple[int, int],
        easing=linear,
    ):
        self.start_position = start_position
        self.end_position = end_position
        self.easing = easing


    def update(self, layer, context: RenderContext):

        progress = self.easing(context.progress)

        start_x, start_y = self.start_position
        end_x, end_y = self.end_position

        layer.transform.x = (
            start_x + (end_x - start_x) * progress
        )

        layer.transform.y = (
            start_y + (end_y - start_y) * progress
        )
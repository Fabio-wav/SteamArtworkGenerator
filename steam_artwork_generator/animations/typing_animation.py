from steam_artwork_generator.animations import Animation
from steam_artwork_generator.models import RenderContext


class TypingAnimation(Animation):

    def __init__(
        self,
        frame_interval: int = 1,
    ) -> None:

        self.frame_interval = max(1, frame_interval)

    def update(self, layer, context: RenderContext) -> None:


        visible_characters = (
            context.frame_index // self.frame_interval
        ) + 1

        visible_characters = min(
            visible_characters,
            len(layer.text),
        )

        layer.render_text = layer.text[:visible_characters]
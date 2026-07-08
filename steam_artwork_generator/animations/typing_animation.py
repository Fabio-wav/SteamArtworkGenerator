from steam_artwork_generator.animations import Animation
from steam_artwork_generator.models import RenderContext


class TypingAnimation(Animation):

    def __init__(
        self,
        start_frame: int = 0,
        frame_interval: int = 1,
    ):
        self.start_frame = start_frame
        self.frame_interval = max(1, frame_interval)

    def update(self, layer, context: RenderContext) -> None:

        if context.frame_index < self.start_frame:
            layer.render_text = ""
            return

        current_frame = context.frame_index - self.start_frame

        visible_characters = (
            current_frame // self.frame_interval
        ) + 1

        visible_characters = min(
            visible_characters,
            len(layer.text),
        )

        layer.render_text = layer.text[:visible_characters]
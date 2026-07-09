from steam_artwork_generator.animations import Animation
from steam_artwork_generator.models import RenderContext


class AnimationClip:

    def __init__(
        self,
        animation: Animation,
        start_frame: int = 0,
        duration: int | None = None,
        enabled: bool = True,
    ):
        self.animation = animation
        self.start_frame = start_frame
        self.duration = duration
        self.enabled = enabled

    def is_active(self, context: RenderContext) -> bool:

        if not self.enabled:
            return False

        if context.frame_index < self.start_frame:
            return False

        if (
            self.duration is not None
            and context.frame_index >= self.start_frame + self.duration
        ):
            return False

        return True

    def update(self, layer, context: RenderContext) -> None:

        if not self.is_active(context):
            return

        local_context = RenderContext(
            frame=context.frame,
            frame_index=context.frame_index - self.start_frame,
            total_frames=context.total_frames,
            duration=context.duration,
        )

        self.animation.update(layer, local_context)
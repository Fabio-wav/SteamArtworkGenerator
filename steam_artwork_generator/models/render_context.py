from dataclasses import dataclass, replace
from PIL.Image import Image


@dataclass
class RenderContext:
    frame: Image
    frame_index: int
    total_frames: int
    duration: int
    progress: float = 0.0

    def copy(self, **changes):
        return replace(self, **changes)
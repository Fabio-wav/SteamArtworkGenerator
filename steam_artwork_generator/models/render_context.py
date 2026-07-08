from dataclasses import dataclass
from PIL.Image import Image


@dataclass
class RenderContext:
    frame: Image
    frame_index: int
    total_frames: int
    duration: int
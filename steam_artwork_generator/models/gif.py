from dataclasses import dataclass
from PIL.Image import Image


@dataclass
class Gif:
    frames: list[Image]
    width: int
    height: int
    duration: int
    loop: int

    @property
    def frame_count(self) -> int:
        return len(self.frames)
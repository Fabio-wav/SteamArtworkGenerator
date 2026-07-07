from dataclasses import dataclass
from PIL.Image import Image

@dataclass
class Frame:
    image: Image
    index: int
    timestamp: float
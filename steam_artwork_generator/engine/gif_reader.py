from pathlib import Path
from PIL import Image

from steam_artwork_generator.models.gif import Gif


class GifReader:

    def __init__(self, path: Path):
        self.path = path

    def read(self) -> Gif:

        image = Image.open(self.path)

        frames = []

        try:
            while True:
                frames.append(image.copy().convert("RGBA"))
                image.seek(image.tell() + 1)
        except EOFError:
            pass
        
        width, height = image.size
        return Gif(
            frames=frames,
            width=width,
            height=height,
            duration=image.info.get("duration", 30),
            loop=image.info.get("loop", 0),
        )
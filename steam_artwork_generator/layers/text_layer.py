from steam_artwork_generator.layers.layer import Layer
from steam_artwork_generator.models.gif import Gif
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

class TextLayer(Layer):

    def __init__(
        self,
        text: str,
        x: int,
        y: int,
        font_path: str,
        font_size: int,
        color: tuple[int, int, int],
    ) -> None:

        self.text = text
        self.x = x
        self.y = y
        self.font_path = font_path
        self.font_size = font_size
        self.color = color

    def apply(self, gif: Gif) -> None:
        for frame in gif.frames:
            draw = ImageDraw.Draw(frame)
            font = ImageFont.truetype(self.font_path, self.font_size)
            draw.text(
                (self.x, self.y),
                self.text,
                font = font,
                fill=self.color
            )
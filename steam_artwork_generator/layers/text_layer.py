from PIL import ImageDraw, ImageFont

from steam_artwork_generator.layers.layer import Layer
from steam_artwork_generator.models import (
    RenderContext,
    TextStyle,
    Transform,
)


class TextLayer(Layer):

    def __init__(
        self,
        text: str,
        style: TextStyle,
        transform: Transform,
    ):
        self.text = text
        self.style = style
        self.transform = transform

        self.font = ImageFont.truetype(
            style.font_path,
            style.font_size
        )

    def draw(self, context: RenderContext):

        draw = ImageDraw.Draw(context.frame)

        draw.text(
            (
                self.transform.x,
                self.transform.y,
            ),
            self.text,
            font=self.font,
            fill=self.style.color,
        )
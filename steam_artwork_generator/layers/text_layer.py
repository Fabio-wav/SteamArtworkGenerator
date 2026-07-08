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
        z_index: int = 0,
        visible_from: int = 0,
        visible_until: int | None = None,
    ):

        super().__init__(
            transform=transform,
            z_index=z_index,
            visible_from=visible_from,
            visible_until=visible_until,
        )

        self.text = text
        self.render_text = text
        self.style = style

        self.font = ImageFont.truetype(
            style.font_path,
            style.font_size
        )
    
    def draw(self, context: RenderContext) -> None:

        draw = ImageDraw.Draw(context.frame)

        draw.text(
            (
                self.transform.x,
                self.transform.y,
            ),
            self.render_text,
            font=self.font,
            fill=self.style.color,
        )
    
    def reset_frame(self):
        self.render_text = self.text
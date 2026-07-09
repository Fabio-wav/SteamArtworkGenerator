from pathlib import Path

from PIL import Image

from steam_artwork_generator.layers.layer import Layer
from steam_artwork_generator.models import (
    RenderContext,
    Transform,
    ImageStyle,
)


class ImageLayer(Layer):

    def __init__(
        self,
        image_path: str,
        style: ImageStyle,
        transform: Transform,
        z_index: int = 0,
        visible_from: int = 0,
        visible_until: int | None = None,
    ) -> None:

        super().__init__(
            transform=transform,
            z_index=z_index,
            visible_from=visible_from,
            visible_until=visible_until,
        )

        self.style = style
        self.image_path = Path(image_path)

        self.image = Image.open(self.image_path).convert("RGBA")

        # Redimensiona somente se informado
        if (
            self.style.width is not None
            and self.style.height is not None
        ):
            self.image = self.image.resize(
                (
                    self.style.width,
                    self.style.height,
                ),
                Image.Resampling.LANCZOS,
            )


    def reset(self):
        pass


    def draw(self, context: RenderContext) -> None:

        image = self.image.copy()

        alpha = image.getchannel("A")
        alpha = alpha.point(
            lambda p: p * self.transform.opacity // 255
        )

        image.putalpha(alpha)

        context.frame.alpha_composite(
            image,
            (
                self.transform.x,
                self.transform.y,
            ),
        )
from steam_artwork_generator.engine.renderer import Renderer
from steam_artwork_generator.scene import Scene

from steam_artwork_generator.layers import ImageLayer
from steam_artwork_generator.models import (
    Transform,
    ImageStyle,
)


def main():

    renderer = Renderer()
    scene = Scene()

    style = ImageStyle(
        width=300,
        height=300,
    )

    image = ImageLayer(
        image_path="assets/images/capetinha.webp",
        style=style,
        transform=Transform(
            x=100,
            y=100,
            opacity=128,
        ),
    )

    scene.add(image)

    renderer.render(
        scene=scene,
        input_path="input/Artwork_Featured.gif",
        output_path="output/opacity_test.gif",
    )


if __name__ == "__main__":
    main()
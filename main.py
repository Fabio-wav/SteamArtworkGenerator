from steam_artwork_generator.engine.renderer import Renderer

from steam_artwork_generator.layers import (
    TextLayer,
    ImageLayer,
)

from steam_artwork_generator.models import (
    TextStyle,
    Transform,
    ImageStyle
)

from steam_artwork_generator.scene import Scene


def main():

    scene = Scene()

    terminal = TextStyle(
        font_path="assets/fonts/consola.ttf",
        font_size=18,
        color=(255, 255, 255),
    )

    scene.add(
        TextLayer(
            text="CAPETINHA.EXE",
            style=terminal,
            transform=Transform(
                x=35,
                y=35,
            ),
        )
    )

    capetinha = ImageStyle(
        width=180,
        height=180,
    )

    scene.add(
        ImageLayer(
            image_path="assets/images/capetinha.webp",
            style=capetinha,
            transform=Transform(
                x=420,
                y=170,
            ),
        )
    )

    Renderer().render(
        scene=scene,
        input_path="input/Artwork_Featured.gif",
        output_path="output/output.gif",
    )


if __name__ == "__main__":
    main()
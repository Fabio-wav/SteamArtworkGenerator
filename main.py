from steam_artwork_generator.engine.renderer import Renderer
from steam_artwork_generator.scene import Scene

from steam_artwork_generator.layers import TextLayer
from steam_artwork_generator.animations import TypingAnimation

from steam_artwork_generator.models import (
    TextStyle,
    Transform,
)


def main():

    renderer = Renderer()
    scene = Scene()

    terminal = TextStyle(
        font_path="assets/fonts/consola.ttf",
        font_size=22,
        color=(255, 255, 255),
    )

    scene.add(
        TextLayer(
            text="CAPETINHA.EXE",
            style=terminal,
            transform=Transform(
                x=40,
                y=40,
            ),
        ).add_animation(
            TypingAnimation(
                frame_interval=2,
            ),
            start_frame=2,
        )
    )

    scene.add(
        TextLayer(
            text="Booting...",
            style=terminal,
            transform=Transform(
                x=40,
                y=80,
            ),
        ).add_animation(
            TypingAnimation(
                frame_interval=2,
            ),
            start_frame=0,
        )
    )

    scene.add(
        TextLayer(
            text="Loading Steam API...",
            style=terminal,
            transform=Transform(
                x=40,
                y=120,
            ),
            visible_from=20,
        ).add_animation(
            TypingAnimation(
                frame_interval=2,
            ),
            start_frame=20,
        )
    )

    renderer.render(
        scene=scene,
        input_path="input/Artwork_Featured.gif",
        output_path="output/output.gif",
    )


if __name__ == "__main__":
    main()
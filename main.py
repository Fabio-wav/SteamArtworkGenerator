from steam_artwork_generator.engine.renderer import Renderer
from steam_artwork_generator.layers import TextLayer


def main():

    renderer = Renderer()

    renderer.add_layer(
        TextLayer(
            text="CAPETINHA.EXE",
            x=40,
            y=40,
            font_path="assets/fonts/consola.ttf",
            font_size=24,
            color=(255, 255, 255)
        )
    )

    renderer.render(
        input_path="input/Artwork_Featured.gif",
        output_path="output/output.gif"
    )


if __name__ == "__main__":
    main()
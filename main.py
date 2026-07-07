from steam_artwork_generator.engine.renderer import Renderer
from steam_artwork_generator.layers import TextLayer


def main() -> None:
    renderer = Renderer()

    renderer.add_layer(TextLayer())

    renderer.render(
        input_path="input/Artwork_Featured.gif",
        output_path="output/output.gif",
    )


if __name__ == "__main__":
    main()
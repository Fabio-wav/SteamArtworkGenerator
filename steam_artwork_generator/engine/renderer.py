from pathlib import Path

from .gif_reader import GifReader
from .gif_writer import GifWriter
from steam_artwork_generator.layers.layer import Layer




class Renderer:
    def __init__(self):
        self.layers: list[Layer] = []

    def add_layer(self, layer: Layer):
        self.layers.append(layer)
        return self
    

    def render(self, input_path: str, output_path: str) -> None:

        input_path = Path(input_path)
        output_path = Path(output_path)

        if not input_path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {input_path.resolve()}"
            )

        print(f"📥 Loading {input_path.name}...")

        gif = GifReader(input_path).read()
        
        print(f"📐 Resolução : {gif.width}x{gif.height}")
        print(f"🎞️  Frames    : {gif.frame_count}")
        print(f"⏱️  Duração   : {gif.duration} ms/frame")
        print(f"🎨 Aplicando {len(self.layers)} layer(s)...")
        for layer in self.layers:
            layer.apply(gif)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)

        GifWriter(output_path).write(gif)

        print(f"✅ GIF salvo em {output_path.resolve()}")
from pathlib import Path

from .gif_reader import GifReader
from .gif_writer import GifWriter
from steam_artwork_generator.scene import Scene
from steam_artwork_generator.models import RenderContext

class Renderer:
    

    def render(self, scene: Scene, input_path: str, output_path: str) -> None:

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
        print(f"🎨 Aplicando {len(scene.layers)} layer(s)...")
        sorted_layers = sorted(
            scene.layers,
            key=lambda layer: layer.z_index
        )
        for frame_index, frame in enumerate(gif.frames):

            context = RenderContext(
                frame=frame,
                frame_index=frame_index,
                total_frames=gif.frame_count,
                duration=gif.duration,
            )

            for layer in sorted_layers:
                layer.reset()
                for clip in layer.clips:
                    if clip.is_active(context):
                        clip.update(layer, context)
                
                if layer.is_visible(context):
                    layer.draw(context)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)

        GifWriter(output_path).write(gif)

        print(f"✅ GIF salvo em {output_path.resolve()}")
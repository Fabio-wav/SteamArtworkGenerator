from pathlib import Path

from steam_artwork_generator.models.gif import Gif


class GifWriter:

    def __init__(self, path: Path):
        self.path = path

    def write(self, gif: Gif):

        gif.frames[0].save(
            self.path,
            save_all=True,
            append_images=gif.frames[1:],
            duration=gif.duration,
            loop=gif.loop,
            disposal=2
        )
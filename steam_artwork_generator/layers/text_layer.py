from steam_artwork_generator.layers.layer import Layer
from steam_artwork_generator.models.gif import Gif


class TextLayer(Layer):

    def apply(self, gif: Gif) -> None:
        print("Aplicando TextLayer...")
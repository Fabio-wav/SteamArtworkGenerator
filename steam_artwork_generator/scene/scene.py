from steam_artwork_generator.layers import Layer


class Scene:

    def __init__(self):
        self.layers: list[Layer] = []

    def add(self, layer: Layer):
        self.layers.append(layer)
        return self
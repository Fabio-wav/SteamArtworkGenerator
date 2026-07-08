class ImageStyle:

    def __init__(
        self,
        width: int | None = None,
        height: int | None = None,
        opacity: float = 1.0,
        rotation: float = 0.0,
    ):
        self.width = width
        self.height = height
        self.opacity = opacity
        self.rotation = rotation
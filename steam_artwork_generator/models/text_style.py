from dataclasses import dataclass


@dataclass
class TextStyle:
    font_path: str
    font_size: int
    color: tuple[int, int, int]
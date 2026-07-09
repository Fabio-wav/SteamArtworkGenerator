from dataclasses import dataclass


@dataclass
class Transform:
    x: int
    y: int
    opacity: int = 255
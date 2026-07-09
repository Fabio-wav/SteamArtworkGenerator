from math import pow


def linear(t: float) -> float:
    return t


def ease_in(t: float) -> float:
    return t * t


def ease_out(t: float) -> float:
    return 1 - pow(1 - t, 2)


def ease_in_out(t: float) -> float:
    if t < 0.5:
        return 2 * t * t

    return 1 - pow(-2 * t + 2, 2) / 2
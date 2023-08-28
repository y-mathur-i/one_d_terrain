"""Interpolation is getting a point between two points
   There are two kinds of interpolation
   1. Linear
   2. cosine
"""
import math


def linear_interpolation(a: int, b: int, mu: int) -> int:
    """Point between a & b at relative distance of mu
      mu ranges between 0 and 1
    """
    return a * (1 - mu) + b * mu


def cosine_interpolation(a: int, b: int, mu: int) -> int:
    """Cosine interpolation creates a smoother curve resulting in less jagged lines
    """
    mu2 = (1 - math.cos(mu * math.pi)) / 2
    return a * (1 - mu2) + b * mu2


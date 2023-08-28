import random
from typing import List


def generate_terrain(count: int, low: int, high: int) -> List[int]:
    """Generate terrain between low and high
       The spikes will look weird and unnatural and jagged
    """
    return list(random.randint(low, high) for _ in range(count))


from dataclasses import dataclass
import numpy as np

@dataclass
class Body:
    name: str
    mass: float
    radius: float
    position: np.ndarray
    velocity: np.ndarray
    shape: str = "sphere"

    def __repr__(self):
        return f"Body({self.name!r}, mass={self.mass}, radius={self.radius})"

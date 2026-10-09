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

    def __repr__(self) -> str:
        return (
            f"Body(name={self.name!r}, mass={self.mass!r}, "
            f"radius={self.radius!r}, position={self.position!r}, "
            f"velocity={self.velocity!r}, shape={self.shape!r})"
        )

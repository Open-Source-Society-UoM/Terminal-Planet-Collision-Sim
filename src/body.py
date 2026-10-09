from dataclasses import dataclass, field

import numpy as np


@dataclass
class Body:
    """Celestial body with mutable kinematic state."""

    name: str
    mass: float
    radius: float
    # Mutable kinematic state — callers update these in place each step.
    acceleration: np.ndarray = field(default_factory=lambda: np.zeros(3))
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))
    shape: str = "sphere"

    def __repr__(self) -> str:
        return (
            f"Body(name={self.name!r}, mass={self.mass!r}, "
            f"radius={self.radius!r}, position={self.position!r}, "
            f"velocity={self.velocity!r}, acceleration={self.acceleration!r}, "
            f"shape={self.shape!r})"
        )

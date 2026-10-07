import numpy as np
from body import Body

def earth_mars():
    earth = Body(
        name="Earth",
        mass=5.972e24,
        radius=6.371e6,
        position=np.array([0.0, 0.0, 0.0]),
        velocity=np.array([0.0, 500.0, 0.0]),
    )
    mars = Body(
        name="Mars",
        mass=6.39e23,
        radius=3.389e6,
        position=np.array([2.0e8, 0.0, 0.0]),
        velocity=np.array([-800.0, 0.0, 0.0]),
    )
    return [earth, mars]

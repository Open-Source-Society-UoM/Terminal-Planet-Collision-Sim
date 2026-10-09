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

def neutronStar_gasGiant():
    neutronStar = Body(
        name="Neutron Star",
        mass=2.68e30, # Average mass according to britannica
        radius=10e3, # Average radius according to britannica
        position=np.array([0.0, 0.0, 0.0]),
        velocity=np.array([1e26, 0.0, 0.0]),
    )
    gasGiant = Body(
        name="Gas Giant",
        mass=1.233e27, # Avg mass of the two gas giants in our solar system.
        radius=64.1e6,
        position=np.array([6e27, 0.0, 0.0]),
        velocity=np.array([-1e26, 0.0, 0.0]),
    )
    return [neutronStar, gasGiant]
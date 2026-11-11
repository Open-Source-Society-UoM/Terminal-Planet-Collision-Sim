import physics
from body import Body


def TEST_no_coll() -> bool:
    a = Body()
    a.position = [0, 0, 0]
    a.radius = 1

    b = Body()
    b.position = [2, 0, 0]
    b.radius = 1

    # Should be false
    return physics.detect_collision(a, b)


def TEST_overlap_coll() -> bool:
    a = Body()
    a.position = [0, 0, 0]
    a.radius = 1

    b = Body()
    b.position = [1, 0, 0]
    b.radius = 1

    # Should be true
    return physics.detect_collision(a, b)


def TEST_coll() -> bool:
    a = Body()
    a.position = [0, 0, 0]
    a.radius = 1

    b = Body()
    b.position = [1, 0, 0]
    b.radius = 2

    # Should be true
    return physics.detect_collision(a, b)

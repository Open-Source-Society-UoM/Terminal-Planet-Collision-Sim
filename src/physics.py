from body import Body


def detect_collision(a: Body, b: Body) -> bool:
    vec = a.position - b.position
    dst = (sum([x*2 for x in vec])) ** 0.5
    return dst <= (a.radius + b.radius)

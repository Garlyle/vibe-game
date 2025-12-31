# map/hexutils.py
def axial_to_cube(q, r):
    x = q
    z = r
    y = -x - z
    return (x, y, z)

def cube_to_axial(x, y, z):
    return (x, z)

HEX_DIRECTIONS = [
    (1, 0), (1, -1), (0, -1),
    (-1, 0), (-1, 1), (0, 1)
]

def neighbors(coord):
    q, r = coord
    return [(q + dq, r + dr) for dq, dr in HEX_DIRECTIONS]

def hex_distance(a, b):
    ax, ay, az = axial_to_cube(*a)
    bx, by, bz = axial_to_cube(*b)

    return max(
        abs(ax - bx),
        abs(ay - by),
        abs(az - bz)
    )

def hex_range(center, radius):
    cq, cr = center
    results = []

    for dq in range(-radius, radius + 1):
        for dr in range(
            max(-radius, -dq - radius),
            min(radius, -dq + radius) + 1
        ):
            results.append((cq + dq, cr + dr))

    return results

def hex_ring(center, radius):
    if radius == 0:
        return [center]

    results = []
    q, r = center

    # start at one corner
    q += HEX_DIRECTIONS[4][0] * radius
    r += HEX_DIRECTIONS[4][1] * radius

    for i in range(6):
        dq, dr = HEX_DIRECTIONS[i]
        for _ in range(radius):
            results.append((q, r))
            q += dq
            r += dr

    return results

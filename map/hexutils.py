import math

# map/hexutils.py
def axial_to_cube(q, r):
    x = q
    z = r
    y = -x - z
    return (x, y, z)

def cube_to_axial(x, y, z):
    return (x, z)

def axial_to_pixel(q, r, size):
    """Convert axial coordinates to pixel (without offset)."""
    x = size * (3/2 * q)
    y = size * (math.sqrt(3) * (r + q/2))
    return x, y

def pixel_to_axial(x, y, size):
    """Convert pixel position to axial (without offset)."""
    q = (2/3 * x) / size
    r = (-1/3 * x + math.sqrt(3)/3 * y) / size
    return q, r


HEX_DIRECTIONS = [
    (1, 0), (1, -1), (0, -1),
    (-1, 0), (-1, 1), (0, 1)
]

def neighbors(coord):
    q, r = coord
    return [(q + dq, r + dr) for dq, dr in HEX_DIRECTIONS]

def hex_vertices(center, size):
    cx, cy = center
    points = []
    for i in range(6):
        angle = math.pi / 3 * i  # 60° increments
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        points.append((x, y))
    return points

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

def cube_round(x, y, z):
    rx = round(x)
    ry = round(y)
    rz = round(z)

    dx = abs(rx - x)
    dy = abs(ry - y)
    dz = abs(rz - z)

    if dx > dy and dx > dz:
        rx = -ry - rz
    elif dy > dz:
        ry = -rx - rz
    else:
        rz = -rx - ry

    return rx, ry, rz

def hex_round(q, r):
    return cube_to_axial(*cube_round(*axial_to_cube(q, r)))

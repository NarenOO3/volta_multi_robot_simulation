def anticlockwise_spiral(n):
    if n <= 0:
        return []

    x, y = 0, 0
    dx, dy = 0, -1
    result = []

    for _ in range(n):
        result.append((x, y))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    return result

def fill_init_poses(n):
    spiral_coords = anticlockwise_spiral(n)
    init_poses = []

    for coord in spiral_coords:
        x, y = coord
        init_poses.append("-x {} -y {} -z 0".format(x, y))

    return init_poses

# Example usage:
n = 5
init_poses = fill_init_poses(n)
print(init_poses)

from math import atan2, sqrt

def solution(dimensions, your_position, guard_position, distance):
    mirrored = [replicated_mirror(your_position, dimensions, distance),replicated_mirror(guard_position, dimensions, distance)]
    directions = set()
    angles_dist = {}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = atan2((your_position[1] - k), (your_position[0] - j))
                length = sqrt((your_position[0] - j) ** 2 + (your_position[1] - k) ** 2)
                if [j, k] != your_position and distance >= length:
                    if (beam in angles_dist and angles_dist[beam] > length) or beam not in angles_dist:
                        if i == 0:
                            angles_dist[beam] = length
                        else:
                            angles_dist[beam] = length
                            directions.add(beam)
    return print(len(directions))


def replicated_mirror(mirrored_room, dimensions, distance):
    temp_mirror = []
    for i in range(len(mirrored_room)):
        values = []
        for j in range(-(distance // dimensions[i]) - 1, (distance // dimensions[i] + 2)):
            values.append(mirroring(j, mirrored_room[i], dimensions[i]))
        temp_mirror.append(values)
    return temp_mirror


def mirroring(mirror, coordinates, dimensions):
    transformed_res = coordinates
    mirror_rotation = [2 * coordinates, 2 * (dimensions - coordinates)]
    if mirror < 0:
        for i in range(mirror, 0):
            transformed_res -= mirror_rotation[(i + 1) % 2]
    else:
        for i in range(mirror, 0, -1):
            transformed_res += mirror_rotation[i % 2]
    return transformed_res





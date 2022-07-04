from typing import Tuple
from itertools import permutations

START_POINT = (0, 2)
POINTS = ((2, 5), (5, 2), (6, 6), (8, 3))


def find_distance(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> float:
    """
    :param point_1: tuple of two integers, which is a point #1
    :param point_2: tuple of two integers, which is a point #2
    :return: distance between two points
    """
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5


def find_min_route(start_point: Tuple[int, int], points: tuple) -> tuple:
    """
    :param start_point: coord of start point
    :param points: tuple of coords of places to visit
    :return: tuple(
            route:tuple of points, which is an optimal route;
            path_distance: dictionary, where key is a point to visit, value is a distance
            )
    """
    min_distance = float('inf')
    path_distance = {}

    for path in permutations(points):

        full_distance = 0
        current_path = {}
        full_distance += find_distance(start_point, path[0])  # between start point and first point in route
        current_path[path[0]] = full_distance

        for i in range(len(path)-1):
            full_distance += find_distance(path[i], path[i+1])
            current_path[path[i+1]] = full_distance

        full_distance += find_distance(start_point, path[-1])  # between last point in route and start point
        current_path[start_point] = full_distance

        if full_distance < min_distance:
            min_distance = full_distance
            path_distance.update(current_path)
            optimal_route = path

    return optimal_route, path_distance


if __name__ == "__main__":
    route, path_distance = find_min_route(START_POINT, POINTS)

    print(START_POINT, end='')
    for point in route:
        print(f"-> {point}[{path_distance[point]}]", end='')
    print(f"-> {START_POINT}[{path_distance[START_POINT]}] = {path_distance[START_POINT]}")

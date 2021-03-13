class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]

        def distance(point_1, point_2):
            return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** (1 / 2)

        distances = set()

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                distances.add(distance(points[i],points[j]))

        if 0 in distances:
            return False

        if len(distances)==2:
            return True

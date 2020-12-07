class Polygon:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.minX = min(point1.x, point2.x, point3.x, point4.x)
        self.maxX = max(point1.x, point2.x, point3.x, point4.x)
        self.minY = min(point1.y, point2.y, point3.y, point4.y)
        self.maxY = max(point1.y, point2.y, point3.y, point4.y)

    def is_inside(self, point):
        return self.minX <= point.x <= self.maxX and self.minY <= point.y <= self.maxY


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inside = False

    def __str__(self):
        return f'Point({self.x},{self.y})'


if __name__ == '__main__':
    shape = Polygon(Point(1, 5), Point(10, 5), Point(1, 1), Point(10, 1))
    points = [Point(3, 3), Point(7, 5), Point(5, 6)]
    for dot in points:
        result = shape.is_inside(dot)
        if result:
            print(f'{dot} is inside polygon')
        else:
            print(f'{dot} is outside polygon')

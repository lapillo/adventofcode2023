def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y

    return inside

# Przykład użycia:
polygon = [(1, 1), (1, 8), (7, 8),(7, 5),(5, 5),(5, 7),(2, 7),(3, 3),(5, 2),(5, 4),(7, 4),(7, 1) ]

point_x = 6
point_y = 2

if point_in_polygon(point_x, point_y, polygon):
    print("Punkt znajduje się wewnątrz obszaru.")
else:
    print("Punkt znajduje się poza obszarem.")
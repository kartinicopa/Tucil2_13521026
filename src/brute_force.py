import math

def eucl_distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(len(p1))))

def brute_force(points):
    global eucl_brute
    eucl_brute = 0
    n = len(points)
    if n <= 1:
        return None
    elif n == 2:
        eucl_brute += 1
        return (points[0], points[1], eucl_distance(points[0], points[1]))
    else:
        min_dist = eucl_distance(points[0], points[1])
        p1 = points[0]
        p2 = points[1]
        for i in range(n):
            for j in range(i+1, n):
                distance = eucl_distance(points[i], points[j])
                eucl_brute += 1
                if distance < min_dist:
                    min_dist = distance
                    p1 = points[i]
                    p2 = points[j]
        return (p1, p2, min_dist)
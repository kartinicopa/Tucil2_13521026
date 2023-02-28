import math

eucl_dnc = 0

def eucl_distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(len(p1))))

def div_conquer(points):
    global eucl_dnc
    n = len(points)
    if n <= 1:
        return None
    elif n == 2:
        eucl_dnc += 1
        distance = eucl_distance(points[0], points[1]) 
        return (points[0], points[1], distance)
    else:
        # Sort points berdasarkan kordinat x
        sortPoint = sorted(points, key=lambda x: x[0])
        midPoint = n // 2
        leftPoint = sortPoint[:midPoint]
        rightPoint = sortPoint[midPoint:]
        # Closest pair yang berada di subarray kiri dan kanan
        leftClosest = div_conquer(leftPoint)
        rightClosest = div_conquer(rightPoint)
        # Cari closest pair yang terdekat
        if leftClosest is None and rightClosest is None:
            closest = None
        elif leftClosest is None:
            closest = rightClosest
        elif rightClosest is None:
            closest = leftClosest
        else:
            closest = leftClosest if leftClosest[2] < rightClosest[2] else rightClosest
        # Closest pair yang berada di antara kedua subarray
        # Sort points berdasarkan kordinat y
        closest_mid = [point for point in sortPoint if abs(point[0] - sortPoint[midPoint][0]) < closest[2]]
        closest_mid = sorted(closest_mid, key=lambda x: x[1])
        for i, point1 in enumerate(closest_mid):
            for point2 in closest_mid[i+1:]: 
                if point2[1] - point1[1] >= closest[2]:
                    break
                distance = eucl_distance(point1, point2)
                eucl_dnc += 1
                if distance < closest[2]:
                    closest = (point1, point2, distance)
        return closest
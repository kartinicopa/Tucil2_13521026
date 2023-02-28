import brute_force
import closest_pair
import random
import time
import platform
import matplotlib.pyplot as plt

def generate_points(n, Rn):
    points = []
    for i in range(n):
        point = []
        for j in range(Rn):
            point.append(random.random())
        points.append(point)
    return points

def splash_screen():
    print("███████████████████████████████████████████████████████████████████████████████")
    print("█─▄▄▄─█▄─▄███─▄▄─█─▄▄▄▄█▄─▄▄─█─▄▄▄▄█─▄─▄─███▄─▄▄─█─▄▄─█▄─▄█▄─▀█▄─▄█─▄─▄─█─▄▄▄▄█")
    print("█─███▀██─██▀█─██─█▄▄▄▄─██─▄█▀█▄▄▄▄─███─██████─▄▄▄█─██─██─███─█▄▀─████─███▄▄▄▄─█")
    print("▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀")
    print("===============================================================================")
    print("===============================================================================")
    print("                            13521026 - Kartini Copa                            ")
    print("===============================================================================")
    print("===============================================================================")

def print_brute_force(points):
    start = time.time()
    p1, p2, min_dist = brute_force.brute_force(points)
    end = time.time()
    print("===============================================================================")
    print("                             Brute Force Algorithm                             ")
    print("===============================================================================")
    print("Closest pair:")
    print("Point 1:", p2)
    print("Point 2:", p1)
    print("Closest distance:", min_dist)
    print("Total euclidean operation:", brute_force.eucl_brute)
    print("Execution time:", "{:.7f}".format(end - start), "seconds")
    
def print_divide_conquer(points):
    start = time.time()
    p1, p2, min_dist = closest_pair.div_conquer(points)
    end = time.time()
    print("===============================================================================")
    print("                           Divide and Conquer Algorithm                        ")
    print("===============================================================================")
    print("Closest pair:")
    print("Point 1:", p1)
    print("Point 2:", p2)
    print("Closest distance:", min_dist)
    print("Total euclidean operation:", closest_pair.eucl_dnc)
    print("Execution time:", "{:.7f}".format(end - start), "seconds")

if __name__ == '__main__':
    splash_screen()
    n = int(input("Enter the number of points: "))
    while n < 2:
        n = int(input("Enter the number of points: "))
    Rn = int(input("Enter the number of dimensions: "))
    points = generate_points(n, Rn)
    
    print_brute_force(points)
    print_divide_conquer(points)
    print("-------------------------------------------------------------------------------")
    print("Operation system:", platform.system(), platform.release())
    print("Processor:", platform.processor())
    print("Node:", platform.node())
    
    closest = closest_pair.div_conquer(points)
    closest_pair_points = [closest[0], closest[1]]  
    
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    if Rn == 2:
        colors = ['#FF1493' if point in closest_pair_points else '#33cccc' for point in points]
        plt.scatter(x, y, c=colors)
    elif Rn == 3:
        z = [point[2] for point in points]
        colors = ['#FF1493' if point in closest_pair_points else '#33cccc' for point in points]
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(x, y, z, c=colors)
    else:
        print("Plotting can only be done in 2D or 3D space.")
    plt.show()

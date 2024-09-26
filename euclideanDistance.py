import math
x1 = int(input("Enter x1:"))
y1 = int(input("Enter y1:"))
x2 = int(input("Enter x2:"))
y2 = int(input("Enter y2:"))

points = [(x1,y1), (x2,y2), (10,16), (5,4)]

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
distances = []
for i in range(len(points)):
    print(i)
    for j in range(i + 1, len(points)):
        print(j)
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(distances)

min_distance = min(distances)
print("Minimum mesafe: ", min_distance)

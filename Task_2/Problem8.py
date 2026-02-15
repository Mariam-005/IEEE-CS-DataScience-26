import math

class Points:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def cross(self, no):
        return Points(
            self.y* no.z -self.z* no.y,
            self.z* no.x -self.x* no.z,
            self.x* no.y -self.y* no.x
        )
    def __sub__(self, no):
        return Points(self.x - no.x,self.y - no.y, self.z -no.z)

    def dot(self, no):
        return self.x* no.x + self.y* no.y + self.z* no.z

        
    def absl(self):
        return pow((self.x** 2 + self.y** 2 + self.z** 2), 0.5)

if __name__ == '__main__':
    points = []
    for i in range(4):
        data = [float(x) for x in input().split()]
        points.append(Points(data[0], data[1], data[2]))

    a, b, c, d = points[0], points[1], points[2], points[3]
    ab = b - a
    bc = c - b
    cd = d - c

    x = ab.cross(bc)
    y = bc.cross(cd)

    cos_PHI = x.dot(y)/(x.absl()* y.absl())

    result = math.degrees(math.acos(cos_PHI))

    print(f"{result:.2f}")


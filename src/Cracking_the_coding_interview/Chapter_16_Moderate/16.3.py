# Intersection: Given two straight line segments (represented as a start point and an end point),
# compute the point of intersection, if any.

# construct the lines in point slope form


class Line:

    def __init__(self, p1, p2=None, slope=None):
        if p2 is None and slope is None:
            raise ValueError("Either 2 points or 1 point + slope is required")
        if p2 is not None and slope is not None:
            raise ValueError("Provide p2 or slope, not both")

        if p2 is None:
            self.slope = slope
        else: # slope is none
            self.slope = (p1[1] - p2[1])/(p1[0] - p2[0])

        self.intercept = self.slope * -1 * p1[0] + p1[1]

    def f(self, x):
        return self.slope * x + self.intercept

    def intersection(self, l2):

        if self.slope == l2.slope: # parallel
            if self.intercept == l2.intercept:  # Same line
                return 0, self.f(0)
            else:
                return None
        else:
            # y = m1 x + b1
            # y = m2 x + b2
            # m1 x + b1 = m2 x + b2
            # x = (b2 - b1)/(m1 - m2)
            x = (l2.intercept - self.intercept)/(self.slope - l2.slope)
            return x, self.f(x)


def compute_intersection_from_points(l1, l2):
    L1, L2 = Line(*l1), Line(*l2)
    return L1.intersection(L2)


print(compute_intersection_from_points([(1, 2), (3, 4)], [(-1, 5), (10, 3)]))

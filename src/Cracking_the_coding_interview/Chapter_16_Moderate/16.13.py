# Bisect Squares: Given two squares on a two-dimensional plane, find a line that would cut these two squares in half.
# Assume that the top and the bottom sides of the square run parallel to the x-axis.

# Math problem! do on paper and pencil first
# first find the middle of each square, then find the line the intersects both centers. Any line through the center of
# a square bisects it

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


def midpoint(p1, p2):
    return (p1[0] + p2[0])/2, (p1[1] + p2[1])/2


def bisect(s1, s2):
    """
    :param s1: diagonal points of s1
    :param s2: diagonal points of s2
    :return: class Line that bisects both squares
    """
    midpoint1, midpoint2 = midpoint(*s1), midpoint(*s2)
    return Line(midpoint1, midpoint2)


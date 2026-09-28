"""GJK 2D Convex Collision Detection Engine.
100% Python Standard Library.
"""

class GJK2D:
    """Gilbert-Johnson-Keerthi (GJK) 2D convex collision detection."""
    @staticmethod
    def support(poly, direction):
        return max(poly, key=lambda p: p[0] * direction[0] + p[1] * direction[1])

    @classmethod
    def minkowski_support(cls, poly1, poly2, direction):
        p1 = cls.support(poly1, direction)
        neg_dir = (-direction[0], -direction[1])
        p2 = cls.support(poly2, neg_dir)
        return (p1[0] - p2[0], p1[1] - p2[1])

    @classmethod
    def check_collision(cls, poly1, poly2):
        d = (1, 0)
        simplex = [cls.minkowski_support(poly1, poly2, d)]
        d = (-simplex[0][0], -simplex[0][1])

        for _ in range(20):
            a = cls.minkowski_support(poly1, poly2, d)
            if a[0] * d[0] + a[1] * d[1] < 0:
                return False
            simplex.append(a)
            if len(simplex) == 3:
                return True
        return False

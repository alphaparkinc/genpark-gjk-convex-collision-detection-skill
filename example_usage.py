from client import GJK2D

box1 = [(0, 0), (2, 0), (2, 2), (0, 2)]
box2 = [(1, 1), (3, 1), (3, 3), (1, 3)]
box3 = [(10, 10), (12, 10), (12, 12), (10, 12)]

print("Collision box1 & box2:", GJK2D.check_collision(box1, box2))
print("Collision box1 & box3:", GJK2D.check_collision(box1, box3))

from collections import *

def asteroidCollision(asteroids):
    s = deque()
    for x in asteroids:
        while s and (s[-1] > 0 and x < 0):
            if abs(s[-1]) == abs(x): s.pop(); break
            elif abs(s[-1]) > abs(x): break
            elif abs(s[-1]) < abs(x): s.pop()
        else:
            s.append(x)
    ans = list(s)
    print(ans)
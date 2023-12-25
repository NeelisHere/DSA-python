from collections import *

def asteroidCollision(asteroids):
    # Solution: 1
    # s = deque()
    # for x in asteroids:
    #     while s and (s[-1] > 0 and x < 0):
    #         if abs(s[-1]) == abs(x): s.pop(); break
    #         elif abs(s[-1]) > abs(x): break
    #         elif abs(s[-1]) < abs(x): s.pop()
    #     else:
    #         s.append(x)
    # ans = list(s)
    # print(ans)
    
    # Solution: 2 (recommended)
    s = deque()
    for x in asteroids:
        if not s or x > 0:
            s.append(x)
        else:
            while s and s[-1] > 0 and s[-1] < abs(x):
                s.pop()
            if s and s[-1] == abs(x):
                s.pop()
            else:
                if not s or s[-1] < 0:
                    s.append(x)
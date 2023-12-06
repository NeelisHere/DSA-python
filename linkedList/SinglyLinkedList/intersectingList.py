def intersectingList(A, B):
    if not A or not B: return None
    p1, p2 = A, B
    while p1 is not p2:
        p1 = p1.next if p1 else B 
        p2 = p2.next if p2 else A
    return p1
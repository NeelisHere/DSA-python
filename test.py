from graphs.detectCycleUndir import detectCycleUndir

g = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2],
    4: [1]
}

detectCycleUndir(g)




    

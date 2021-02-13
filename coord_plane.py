
def line_test(coord1, coord2, x_coord): 
    slope = (coord1[1]-coord2[1])/(coord1[0]-coord2[0]) 
    y = slope*(x_coord-coord1[0]) + coord1[1]
    print(y)
    return y 

if __name__ == "__main__": 
    line_test((0,0), (4,4), 1)

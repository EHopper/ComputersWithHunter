"""
Making a square around a hole of side length n requires (n + 1) * 4 tiles
The new square has sides of size n + 2
"""

def square(n):


    n_squares = 0
    for hole_size in range(1, n // 4):
        n_squares += recf(n, hole_size)

    return n_squares

def recf(n, hole_size):
    if n < calc_tiles_around_hole(hole_size):
        #print('too small')
        return 0
    if n == calc_tiles_around_hole(hole_size):
        #print('spot on')
        return 1


    return 1 + recf(n - calc_tiles_around_hole(hole_size),
                    hole_size + 2)

def calc_tiles_around_hole(hole_size):
    return (hole_size + 1) * 4

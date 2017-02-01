from Piece import Piece
from Puzzle import Puzzle

pieces = [
    Piece( [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0], [1, 1, 0]] ),
    Piece( [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0]] ),
    Piece( [[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 2, 0]] ),
    Piece( [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 1, 0]] ),
    Piece( [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 1, 0], [1, 1, 1]] ),
    Piece( [[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 2, 0], [1, 1, 0]] )
    ]

q = Puzzle(pieces, 3,3,3)
q.solve()

print("There are {!s} solutions.\nPlotting one of them..".format(q.number_of_solutions/24))

q.plot_solution()

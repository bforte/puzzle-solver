# puzzle-solver
Solves 3d puzzles (and thus 2d ones as well) by using Knuth's algorithm X (dancing links implementation).

At the moment this only solves puzzles that can be represented by cubes (or squares).

# Implementation

A Piece is basically just a list of 3-dimensional coordinates that it consists of.

A puzzle consists of a list of Pieces and dimensions; once `solve()` is called it populates a binary matrix that describes the puzzle's corresponding exact cover problem instance. This is then solved by [dlx-python](https://github.com/bforte/dlx-python).

Once a puzzle is solved you can plot its solutions with the function `plot_solution` this will build a graph of the pieces, st. there is an edge from one piece to another if and only if their surfaces touch and colors that graph to determine a suitable coloring scheme for the solution.

# Example

```
>>> from Piece import Piece
>>> from Puzzle import Puzzle
```

To create a piece (T pentomino) simply call something like:

```
>>> p = Piece( [[0,0,0], [0,1,0], [0,2,0], [-1,1,0], [-2,1,0]] )
```

To get an idea for how the piece looks like call:

```
>>> p.plot()
```
![Image of the just created Piece p](https://github.com/bforte/puzzle-solver/blob/master/imgs/T.png)

Once you got a list of pieces (`pentominos`) and want to solve a 5x6x2 puzzle, call:

```
>>> q = Puzzle(pentominos, 5,4,3)
>>> q.solve()
>>> q.number_of_solutions
2112
>>> q.plot_solution()
```
![Image of a solution to the just created puzzle](https://github.com/bforte/puzzle-solver/blob/master/imgs/6x5x2-803.png)

**Note**: `q.number_of_solutions` counts every solution, even if it's just a rotation of another one etc.

See the `__main__` in `Puzzle.py` for a full example.

# Credits

Thanks [jlaire](https://github.com/jlaire) for the awesome dancing links implementation and to [eliasdorneles](https://github.com/eliasdorneles) (graph_coloring.py).

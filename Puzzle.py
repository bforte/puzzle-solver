import dlx_python.libexactcover as ec
from graph_coloring import find_graph_colors,generate_dot
from Grid import Grid
from Piece import Piece

from PIL import Image, ImageDraw
from random import randint

class Puzzle:

    """
    Puzzle consists of dimensions and n pieces

    Args:
        pieces (Piece[]): List of n pieces
        x (int): Depth of the puzzle
        y (int): Width of the puzzle
        z (int): Height of the puzzle

    """

    def __init__(self, pieces, x,y,z):
        # Set pieces
        self.pieces = pieces
        self.num_pieces = len(self.pieces)

        self.x = x
        self.y = y
        self.z = z

    def populate_matrix(self):
        """
        Populate a boolean matrix by mapping the 3d space to
         a 1d space and adding one coordinate for each real piece.
        """

        # Projection from R3 to R1
        proj1d = lambda x: x[0] + self.x*x[1] + self.x*self.y*x[2]

        # The boolean matrix
        self.boolean_matrix = []

        # Store the placed pieces coordinates for plotting
        self.p_pieces = { }
        key = 0

        # Loop over every piece
        for (i,piece) in enumerate(self.pieces):

            # and each possible position/rotation of that piece
            for cover in piece.get_all_positions(self.x,self.y,self.z):

                # Project the coordinates to 1d
                projection = map(proj1d, cover)

                # Store only the real coordinates of the pieces
                self.p_pieces[key] = cover
                key += 1

                # Generate a fresh 0-row
                row = [ 0 for _ in range(self.x*self.y*self.z+self.num_pieces) ]

                # Set value to 1 in row for each projected coordinate and for the virtual coordinate
                for r_idx in projection:
                    row[r_idx] = 1
                row[self.x*self.y*self.z+i] = 1

                self.boolean_matrix.append(row)

    def solve(self):
        """ Try to solve the current puzzle and return boolean """

        # Populate the matrix
        self.populate_matrix()

        # Call the C++ dlx-module to solve the exact cover
        s = ec.Solution(self.boolean_matrix)
        self.solutions = s.solutions
        self.number_of_solutions = s.number_of_solutions

        return self.number_of_solutions > 0

    def plot_solution(self, solution=1984, save=False):
        """ Plot solution """

        # Set default
        if solution == 1984:
            n = randint(0,len(self.solutions))
            solution = self.solutions[n]

        # Create grid
        grid = Grid(self.x,self.y,self.z)

        # Loop over solution coordinates and set GridNode to p_piece key
        for vkey in solution:
            # Loop over all blocks
            for x,y,z in self.p_pieces[vkey]:

                # Set the vkey of the GridNode
                grid[x,y,z].set_vkey(vkey)

        palette = [
                    (234,213,73),
                    (121,106,226),
                    (37,115,0),
                    (147,0,118),
                    (231,132,39),
                    (53,17,92),
                    (255,154,223),
                    (130,0,33)
                  ]

        # Initialize graph
        graph = { vkey : [] for vkey in solution }

        # Build the graph for coloring the pieces
        for i in range(self.x):
            for j in range(self.y):
                for k in range(self.z):
                    cur = grid[i,j,k]
                    # Loop over all neighbours of each GridNode
                    for n in cur.get_neighbours():
                        # If neighbour is another new piece, we add it to the graph
                        if n.vkey != cur.vkey and n.vkey not in graph[cur.vkey]:
                            graph[cur.vkey].append(n.vkey)

        # Determine the graphs color
        colors = find_graph_colors(graph)

        # Create vkey2color dictionary
        vkey2color = { v: palette[c] for (v,c) in generate_dot(graph, colors).viewitems() }

        # Generate an image
        blockwidth = 50
        WIDTH = blockwidth*(self.x+2)
        HEIGHT = (self.z-1)*blockwidth/10 + (self.y*self.z+2)*blockwidth

        im = Image.new('RGBA', (WIDTH, HEIGHT), (255,255,255,255))
        draw = ImageDraw.Draw(im)

        # Loop over each GridNode and plot it
        for k in range(self.z):
            for i in range(self.x):
                for j in range(self.y):

                    # Calculate the location where to draw a block
                    ax, ay =  blockwidth*(i+1), blockwidth*(j+1)  + k*(blockwidth*self.y+blockwidth/10)
                    bx, by = ax+blockwidth, ay+blockwidth

                    # Draw a square with the correct color
                    draw.rectangle((ax,ay, bx,by), vkey2color[grid[i,j,k].vkey])

        if save:

            # Save the image to file
            solution_num = self.solutions.index(solution)
            fname = 'x'.join(map(str,[self.x,self.y,self.z])) +'-'+ str(solution_num)+'.png'
            print("Saving to imgs/{!s}".format(fname))
            with open('imgs/'+fname, 'w') as f:
                im.save(f)
        else:

            # Show the picture on screen
            im.show()


    def plot_pieces(self):
        """ Plot all the pieces (useful for debugging) """

        for (i,p) in enumerate(self.pieces):
            p.plot(plt_num=i)

if __name__ == '__main__':

    pentominos = [
        Piece( [[0,0,0], [0,1,0], [0,2,0], [1,1,0], [2,1,0]] ),
        Piece( [[0,0,0], [0,1,0], [0,2,0], [0,3,0], [0,4,0]] ),
        Piece( [[0,0,0], [0,1,0], [0,2,0], [-1,1,0],[1,1,0]] ),
        Piece( [[0,0,0], [0,1,0], [1,1,0], [1,2,0], [1,3,0]] ),
        Piece( [[0,0,0], [1,0,0], [0,1,0], [0,2,0], [0,3,0]] ),
        Piece( [[0,0,0], [1,1,0], [0,1,0], [0,2,0], [0,3,0]] ),
        Piece( [[0,0,0], [0,1,0], [0,2,0], [-1,0,0],[1,2,0]] ),
        Piece( [[0,0,0], [0,1,0], [0,2,0], [1,0,0], [2,0,0]] ),
        Piece( [[0,0,0], [1,1,0], [1,2,0], [0,1,0], [0,2,0]] ),
        Piece( [[0,0,0], [0,1,0], [1,1,0], [1,2,0], [2,2,0]] ),
        Piece( [[0,0,0], [0,1,0], [0,2,0], [1,0,0], [1,2,0]] ),
        Piece( [[0,0,0], [0,1,0], [1,1,0], [1,2,0], [2,1,0]] )
        ]

    dimensions = [ (10,6,1),(12,5,1),(15,4,1),(20,3,1), # 2d
                   (5,4,3),(6,5,2),(10,3,2) ]           # 3d

    # Solve the pentominos for all possible dimension triples
    for x,y,z in dimensions:

        q = Puzzle(pentominos, x,y,z)

        q.solve()
        q.plot_solution(save=True)

        n = q.number_of_solutions/4

        print("{!s}x{!s}x{!s} has {!s} solutions\n".format(x,y,z,n))

import numpy as np
from rotation import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def add_offset(blocks, x,y,z):
    return [ [a+x,b+y,c+z] for a,b,c in blocks ]

def fits(possible_placement, x,y,z):
    for a,b,c in possible_placement:
        if a < 0 or x <= a:
            return False
        if b < 0 or y <= b:
            return False
        if c < 0 or z <= c:
            return False
    return True

class Piece:

    """
    A piece is just a list of (x,y,z) coordinates  (right-handed)

    Args:
        blocks ((int,int,int)[]): List of coordinate points

    """

    def __init__(self, blocks):
        """ Initialize a Piece """

        # Ensure that one position is only used once
        self.init_blocks = []
        for b in blocks:
            if b not in self.init_blocks:
                self.init_blocks.append(b)
        self.init_blocks.sort()

        # Generate all the distinct placements of this piece
        self.distinct_placements = []
        self.generate_distinct_placements()

    def rotate(self, n):
        """ Rotate the piece by one of the 24 rotations """

        return [np.dot(rotation_matrix(n), b).tolist() for b in self.init_blocks]

    def generate_distinct_placements(self):
        """
        Generate all possible rotations and move most each Piece st.
         'most negative piece' is at (0,0,0). This way we can generate
         an as small as possible list of distinct possible placements.
        """

        # Loop over all possible rotations
        for rot in range(24):
            rotated_block = self.rotate(rot)

            # Get the min-block and its offset
            (min_x,min_y,min_z) = min(rotated_block)

            # Add offset to all blocks
            moved_block = [ [x-min_x, y-min_y, z-min_z] for x,y,z in rotated_block ]
            moved_block.sort()

            # Add it if not already generated
            if moved_block not in self.distinct_placements:
                self.distinct_placements.append(moved_block)

    def get_all_positions(self, x,y,z):
        """
        Generate all possible positions and rotations st.
         the piece still fits an x*y*z game.
        """

        valid = []

        # Loop over all possible offsets
        for offset_x in range(x):
            for offset_y in range(y):
                for offset_z in range(z):
                    # Loop over all possible rotations
                    for rot_piece in self.distinct_placements:

                        # Generate absolute coordinates
                        possible_placement = add_offset(
                            rot_piece,
                            offset_x,offset_y,offset_z
                            )

                        # If placement is in bounds, add to valid placements
                        if fits(possible_placement, x,y,z):
                            valid.append(possible_placement)

        return valid

    def __str__(self):
        return "Piece( [ {!s} ] )".format( ', '.join(map(str,self.init_blocks)))

    def __eq__(self, other):
        # Create all placements to compare
        other.generate_distinct_placements()
        self.generate_distinct_placements()

        for plcmnt in other.distinct_placements:
            if plcmnt in self.distinct_placements:
                return True
        return False

    """
    The following methods are just matplotlib-plot functions for
    easier debugging..
    """

    def plot_block(self, ax, x,y,z):
        """
        Plots one (x,y,z) block

        Args:
            ax (subplot): The matplotlib object responsible for plotting
            x,y,z (int): The coordinates of the block center
        """

        r = [-0.5,0.5]
        X, Y = np.meshgrid(r, r)

        # Plot all six surfaces
        ax.plot_surface(   X+x,   Y+y, z + 0.5, alpha=0.5)
        ax.plot_surface(   X+x,   Y+y, z - 0.5, alpha=0.5)
        ax.plot_surface(   X+x,-0.5+y, z +   Y, alpha=0.5)
        ax.plot_surface(   X+x, 0.5+y, z +   Y, alpha=0.5)
        ax.plot_surface( 0.5+x,   X+y, z +   Y, alpha=0.5)
        ax.plot_surface(-0.5+x,   X+y, z +   Y, alpha=0.5)

        max_range = max(x,y,z)
        mid_x = 0.5
        mid_y = 0.5
        mid_z = 0.5
        ax.set_xlim(mid_x -.1 - max_range, mid_x +.1 + max_range)
        ax.set_ylim(mid_y -.1 - max_range, mid_y +.1 + max_range)
        ax.set_zlim(mid_z -.1 - max_range, mid_z +.1 + max_range)


    def plot_blocks(self, blocks, i, x=0,y=0,z=0):
        """ Plots a whole array of blocks and blocks """

        fig = plt.figure(i)

        ax = fig.add_subplot(111, projection='3d')

        for (a,b,c) in blocks:
          self.plot_block(ax, a,b,c)

        if x != 0 or y != 0 or z != 0:
            x += .5
            y += .5
            z += .5

            ax.scatter3D([-0.5,x,x,-0.5,-0.5,x,x,0],
                         [-0.5,-0.5,y,y,-0.5,-0.5,y,y],
                         [-0.5,-0.5,-0.5,-0.5,z,z,z,z], color='red')

        ax.set_aspect('equal')
        ax.set_axis_off()
        plt.show()

    def plot(self, plt_num=0):
        self.plot_blocks(self.distinct_placements[0], plt_num)
        plt.show()

    def plot_all_rotations(self):
        """ Plots all possible rotations of current piece """
        self.num_figs = 0

        for i in range(24):
            self.plot_blocks(p.rotate(i), self.num_figs)
            self.num_figs += 1

        plt.show()

    def plot_all_distinct(self):
        """ Plots all distinct placements of current piece """
        self.num_figs = 0

        for p in self.distinct_placements:
            self.plot_blocks(p, self.num_figs)
            self.num_figs += 1

        plt.show()

if __name__ == '__main__':
    """
    This script demonstrates the Piece object a bit,
     it generates all distinct placements of a small
     piece and plots all of the possibilities.
    """
    blocks = [[0,0,0], [0,0,1], [0,1,0]]
    p = Piece(blocks)
    p.plot_all_distinct()
    print len(p.distinct_placements)

from GridNode import GridNode

class Grid:
    """
    This class describes an x*y*z grid which
     consists of GridNodes
    """
    def __init__(self, x,y,z):
        self.dim = (x,y,z)
        self.nodes = []

        for i in range(x):
            self.nodes.append([])
            for j in range(y):
                self.nodes[i].append([])
                for k in range(z):

                    # Create GridNodes
                    g = GridNode(i,j,k, x,y,z)
                    self.nodes[i][j].append(g)

        for i in range(x):
            for j in range(y):
                for k in range(z):

                    # Loop over all nodes in Grid
                    cur = self.nodes[i][j][k]

                    # Set all neighbours
                    for n in range(6):
                        if cur.has(n):
                            if n == 0:
                                cur.set_n(n, self.nodes[i][j][k-1])
                            elif n == 1:
                                cur.set_n(n, self.nodes[i+1][j][k])
                            elif n == 2:
                                cur.set_n(n, self.nodes[i][j][k+1])
                            elif n == 3:
                                cur.set_n(n, self.nodes[i-1][j][k])
                            elif n == 4:
                                cur.set_n(n, self.nodes[i][j+1][k])
                            elif n == 5:
                                cur.set_n(n, self.nodes[i][j-1][k])

    def __getitem__(self, (x,y,z)):
        if 0 <= x and x < self.dim[0] and \
           0 <= y and y < self.dim[1] and \
           0 <= z and z < self.dim[2]:
            return self.nodes[x][y][z]
        else:
            return None

if __name__ == '__main__':
    grid = Grid(5,6,2)
    print grid[0,1,0].get_neighbours()

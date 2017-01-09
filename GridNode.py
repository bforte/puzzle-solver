
class GridNode:
    """
    This class describes a GridNode which has 6 neighbours
    """
    def __init__(self, x,y,z, dim_x,dim_y,dim_z):
        self.coord = (x,y,z)
        self.dim = (dim_x,dim_y,dim_z)
        self.neighbours = [None for i in range(6)]

    def get_neighbours(self):
        return [ n for n in self.neighbours if n != None ]

    def set_vkey(self, s):
        self.vkey = s

    def set_n(self, n, other):
        if 0 <= n and n < 6:
            self.neighbours[n] = other

    def has(self, n):
        if n == 0:
            return self.coord[2]-1 in range(self.dim[2])
        elif n == 1:
            return self.coord[0]+1 in range(self.dim[0])
        elif n == 2:
            return self.coord[2]+1 in range(self.dim[2])
        elif n == 3:
            return self.coord[0]-1 in range(self.dim[0])
        elif n == 4:
            return self.coord[1]+1 in range(self.dim[1])
        elif n == 5:
            return self.coord[1]-1 in range(self.dim[1])
        else:
            return False

    def __str__(self):
        return "GridNode" + str(self.coord)
    def __repr__(self):
        return "GridNode" + str(self.coord)

    def __getitem__(self, n):
        if self.has(n):
            return self.neighbours[n]
        else:
            return None

if __name__ == '__main__':
    g = GridNode(0,0,0, 5,6,2)
    print g[0]
    print g[138]

import numpy as np
global ROTATION_MATRICES


""" Hard coded rotation matrices for fast access """

ROTATION_MATRICES = [
        np.array( [[0, 1, 0], [0, 0, 1], [1, 0, 0]] ),
        np.array( [[0, 0, 1], [0, 1, 0], [-1, 0, 0]] ),
        np.array( [[-1, 0, 0], [0, 0, -1], [0, -1, 0]] ),
        np.array( [[0, 0, 1], [0, -1, 0], [1, 0, 0]] ),
        np.array( [[0, 0, 1], [1, 0, 0], [0, 1, 0]] ),
        np.array( [[0, 0, -1], [0, -1, 0], [-1, 0, 0]] ),
        np.array( [[-1, 0, 0], [0, -1, 0], [0, 0, 1]] ),
        np.array( [[-1, 0, 0], [0, 0, 1], [0, 1, 0]] ),
        np.array( [[0, 0, -1], [0, 1, 0], [1, 0, 0]] ),
        np.array( [[0, -1, 0], [-1, 0, 0], [0, 0, -1]] ),
        np.array( [[0, -1, 0], [1, 0, 0], [0, 0, 1]] ),
        np.array( [[-1, 0, 0], [0, 1, 0], [0, 0, -1]] ),
        np.array( [[0, 0, -1], [1, 0, 0], [0, -1, 0]] ),
        np.array( [[1, 0, 0], [0, 0, 1], [0, -1, 0]] ),
        np.array( [[1, 0, 0], [0, 1, 0], [0, 0, 1]] ),
        np.array( [[0, 1, 0], [-1, 0, 0], [0, 0, 1]] ),
        np.array( [[0, 0, -1], [-1, 0, 0], [0, 1, 0]] ),
        np.array( [[0, -1, 0], [0, 0, -1], [1, 0, 0]] ),
        np.array( [[0, 1, 0], [1, 0, 0], [0, 0, -1]] ),
        np.array( [[1, 0, 0], [0, -1, 0], [0, 0, -1]] ),
        np.array( [[0, -1, 0], [0, 0, 1], [-1, 0, 0]] ),
        np.array( [[1, 0, 0], [0, 0, -1], [0, 1, 0]] ),
        np.array( [[0, 0, 1], [-1, 0, 0], [0, -1, 0]] ),
        np.array( [[0, 1, 0], [0, 0, -1], [-1, 0, 0]] )
        ]

def rotation_matrix(n):
    """
    Lookup the 'the' hard-coded rotation matrix

    Args:
        n (int): Number of rotation [0,24)
    """
    if n < 0 or 23 < n:
        print("rotation_matrix: n (" + str(n) + ") not in [0,24]")
        return None
    else:
        return ROTATION_MATRICES[n]

import numpy as np
import matplotlib.pyplot as plt


def connectivity_mgrid(nx, ny):
    connectivity = []
    total_elements = 0
    for i in range(ny):
        for j in range(nx):
            # one element
            connectivity.append(
                i * (nx+1) + j
            )
            connectivity.append(
                i * (nx+1) + j + 1
            )
            connectivity.append(
                (i + 1) * (nx+1) + j + 1
            )

            # another element
            connectivity.append(
                i * (nx+1) + j
            )
            connectivity.append(
                (i + 1) * (nx+1) + j
            )
            connectivity.append(
                (i + 1) * (nx+1) + j + 1
            )

            total_elements += 2

    return connectivity, total_elements


class Mesh:
    """
    Connectivity is of length (nx + 1)*(ny+1)*3 . Each elements connectivity
    information is given by 3 consecutive indices.

    """
    def __init__(self, nx, ny, x, y, connectivity, total_elements):
        self.nx = nx
        self.ny = ny
        self.x = x
        self.y = y
        self.connectivity = connectivity
        self.total_elements = total_elements

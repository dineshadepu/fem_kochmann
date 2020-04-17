import numpy as np
from mesh import Mesh, connectivity_mgrid


def test_mesh_nodes():
    nx = 4
    ny = 4
    x, y = np.mgrid[0: 2.: complex(nx+1), 0: 2.: complex(ny+1)]
    x = x.ravel()
    y = y.ravel()

    conn, tot_ele = connectivity_mgrid(nx, nx)

    fem_mesh = Mesh(nx, ny, x, y, conn, tot_ele)

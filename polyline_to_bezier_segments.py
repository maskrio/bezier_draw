import numpy as np
def polyline_to_bezier_segments(points, n_segments):
    pts = points.copy()
    N = pts.shape[0]

    grid = np.linspace(0, N - 1, n_segments + 1, dtype=int)

    seg_rows = []

    for k in range(n_segments):
        idx0 = grid[k]
        idx3 = grid[k + 1]

        P0 = pts[idx0]
        P3 = pts[idx3]

        span = idx3 - idx0

        idx1 = idx0 + span // 3
        idx2 = idx0 + 2 * span // 3
        P1 = pts[idx1]
        P2 = pts[idx2]

        seg_rows.append([P0[0], P0[1], P1[0], P1[1], P2[0], P2[1], P3[0], P3[1]])

    segments = np.array(seg_rows, dtype=float)
    return segments